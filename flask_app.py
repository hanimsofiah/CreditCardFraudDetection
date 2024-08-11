from flask import Flask, request, render_template, jsonify,send_from_directory
import pandas as pd
import pickle
import xgboost as xgb
import logging

app = Flask(__name__)


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    model = pickle.load(open('development/xgboost/model.pkl', 'rb'))
    scaler = pickle.load(open('development/xgboost/scaler.pkl', 'rb'))
    model_loaded = "Model Loaded Successfully"
except Exception as e:
    model = None
    scaler = None
    model_loaded = f"Failed To Load Model: {e}"
    model_features = None

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route('/bulk_upload', methods=['GET', 'POST'])
def bulk_upload():
    if request.method == 'GET':
        return render_template('bulk_upload.html')
    elif request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            try:
                data = pd.read_csv(file)
                logging.debug("Uploaded data columns: %s", data.columns.tolist())

                if not model:
                    logging.error("Model is not loaded")
                    return jsonify({"error": "Model is not loaded"}), 500

                required_features = [f'V{i}' for i in range(1, 29)] + ['scaled_amount']
                if not all(feature in data.columns for feature in required_features):
                    missing_features = [feature for feature in required_features if feature not in data.columns]
                    logging.error("Missing features: %s", missing_features)
                    return jsonify({"error": f"Missing features: {missing_features}"}), 400

                dmatrix = xgb.DMatrix(data[required_features])
                predictions = model.predict(dmatrix)
                data['Prediction'] = ['Fraud' if pred > 0.5 else 'Non-Fraud' for pred in predictions]

                numeric_columns = data.columns.difference(['Prediction'])
                data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='coerce')
                
                fraud_count = sum(data['Prediction'] == 'Fraud')
                non_fraud_count = sum(data['Prediction'] == 'Non-Fraud')

                html_table = data.to_html(classes='table table-striped', index=False, escape=False)
                return jsonify({
                    "html_table": html_table,
                    "fraud_count": fraud_count,
                    "non_fraud_count": non_fraud_count
                })
            except Exception as e:
                logging.error("Error processing file: %s", str(e))
                return jsonify({"error": str(e)}), 500
        else:
            logging.error("No file or incorrect file type")
            return jsonify({"error": "No file or incorrect file type"}), 400


@app.route('/', methods=['GET', 'POST'])
def home():
    feature_values = {f'V{i}': '0' for i in range(1, 29)}
    amount = '0'
    result = None
    confidence = None

    if request.method == 'POST':
        print("Received POST data:", request.form)  
        try:
            feature_values = {f'V{i}': float(request.form.get(f'V{i}', '0')) for i in range(1, 29)}
            amount = float(request.form.get('amount', '0'))

            features_list = [float(feature_values[f'V{i}']) for i in range(1, 29)]
            features_df = pd.DataFrame([features_list], columns=[f'V{i}' for i in range(1, 29)])
            scaled_amount = scaler.transform([[float(amount)]])[0][0]
            features_df['scaled_amount'] = scaled_amount

            for i, value in enumerate(features_list, 1):
                decimal_part = str(value).split('.')[1] if '.' in str(value) else ''
                feature_values[f'V{i}'] = format(value, '.{}f'.format(len(decimal_part)))

            dmatrix = xgb.DMatrix(features_df)

            prediction_proba = model.predict(dmatrix)[0]
            confidence = f"{prediction_proba * 100:.2f}%"
            result = 'Fraud' if prediction_proba > 0.5 else 'Non-Fraud'

        except Exception as e:
            result = "Error processing your request"
            confidence = str(e)

    return render_template('index.html', prediction=result, confidence=confidence, model_loaded=model_loaded, 
                           feature_values=feature_values, amount=amount)


if __name__ == '__main__':
    app.run(debug=True)
