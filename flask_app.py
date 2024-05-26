"""
from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
import os
import xgboost as xgb  # Ensure xgboost is imported

app = Flask(__name__)

# Attempt to load the model and scaler
try:
    model = pickle.load(open('development/xgboost/model.pkl', 'rb'))
    scaler = pickle.load(open('development/xgboost/scaler.pkl', 'rb'))
    model_loaded = "Model Loaded Successfully"
except Exception as e:
    model = None
    scaler = None
    model_loaded = f"Failed To Load Model: {e}"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            transactions = request.form['transactions']
            amount = float(request.form['amount'])

                        # Convert transaction and amount inputs
            transaction_list = [float(x) for x in transactions.split(',')]
            scaled_amount = scaler.transform([[amount]])[0][0]
            transaction_list.append(scaled_amount)
            
            columns = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 
                       'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 
                       'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'scaled_amount']
            
            features_df = pd.DataFrame([transaction_list], columns=columns)
            dmatrix = xgb.DMatrix(features_df)
            
            # Get prediction probability
            prediction_proba = model.predict(dmatrix)[0]
            confidence = f"{prediction_proba * 100:.2f}%"
            result = 'Fraud' if prediction_proba > 0.5 else 'Non-Fraud'

            # Return the rendered template with form values and prediction results
            return render_template('index.html', prediction=result, confidence=confidence, 
                                   model_loaded=model_loaded, transactions=transactions, amount=amount)
        except Exception as e:
            # Return the template with an error message, retaining the input values
            return render_template('index.html', prediction=f"Error: {str(e)}", model_loaded=model_loaded, 
                                   transactions=transactions, amount=amount)
    else:
        # For a GET request, render the template with empty values for the form
        return render_template('index.html', model_loaded=model_loaded, transactions='', amount='')

if __name__ == '__main__':
    app.run(debug=True)

"""
from flask import Flask, request, render_template, redirect, url_for, flash
import pandas as pd
import pickle
import os
import xgboost as xgb

app = Flask(__name__)

# Load the model and scaler
try:
    model = pickle.load(open('development/xgboost/model.pkl', 'rb'))
    scaler = pickle.load(open('development/xgboost/scaler.pkl', 'rb'))
    model_loaded = "Model Loaded Successfully"
except Exception as e:
    model = None
    scaler = None
    model_loaded = f"Failed To Load Model: {e}"

@app.route('/', methods=['GET', 'POST'])
def home():
    # Default values
    feature_values = {f'V{i}': '0' for i in range(1, 29)}
    amount = '0'
    result = None
    confidence = None

    if request.method == 'POST':
        print("Received POST data:", request.form)  
        try:
            # Extract and convert features and amount from the form
            feature_values = {f'V{i}': float(request.form.get(f'V{i}', '0')) for i in range(1, 29)}
            amount = float(request.form.get('amount', '0'))

            # Convert all features to float and maintain original decimal places for display
            features_list = [float(feature_values[f'V{i}']) for i in range(1, 29)]
            features_df = pd.DataFrame([features_list], columns=[f'V{i}' for i in range(1, 29)])
            scaled_amount = scaler.transform([[float(amount)]])[0][0]
            features_df['scaled_amount'] = scaled_amount

            # Updating feature_values with formatted strings to preserve decimal places
            for i, value in enumerate(features_list, 1):
                decimal_part = str(value).split('.')[1] if '.' in str(value) else ''
                feature_values[f'V{i}'] = format(value, '.{}f'.format(len(decimal_part)))

            # Convert DataFrame to DMatrix
            dmatrix = xgb.DMatrix(features_df)

            # Make prediction
            prediction_proba = model.predict(dmatrix)[0]
            confidence = f"{prediction_proba * 100:.2f}%"
            result = 'Fraud' if prediction_proba > 0.5 else 'Non-Fraud'

        except Exception as e:
            result = "Error processing your request"
            confidence = str(e)

    return render_template('index.html', prediction=result, confidence=confidence, model_loaded=model_loaded, 
                           feature_values=feature_values, amount=amount)

@app.route('/bulk_upload', methods=['GET', 'POST'])
def bulk_upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            data = pd.read_csv(file)
            
            # Ensure the DataFrame matches the model's expected features
            features_df = data  # Assuming the data already includes 'scaled_amount' as the last column correctly
            
            dmatrix = xgb.DMatrix(features_df)
            predictions = model.predict(dmatrix)
            
            # Adding predictions to DataFrame
            data['Prediction'] = ['Fraud' if pred > 0.5 else 'Non-Fraud' for pred in predictions]
            
            # Calculate statistics for visualization
            fraud_count = sum(pred > 0.5 for pred in predictions)
            non_fraud_count = len(predictions) - fraud_count
            
            # Convert DataFrame to HTML, ensure HTML is not escaped
            html_table = data.to_html(classes='table table-striped', index=False, escape=False)
            return render_template('results.html', table=html_table, fraud_count=fraud_count, non_fraud_count=non_fraud_count)
    return render_template('bulk_upload.html')

if __name__ == '__main__':
    app.run(debug=True)
