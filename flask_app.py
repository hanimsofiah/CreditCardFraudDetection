from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
import os
import xgboost as xgb  # Ensure xgboost is imported

app = Flask(__name__)

# Attempt to load the model and scaler
try:
    model = pickle.load(open('development/xgboost/model.pkl', 'rb'))
    scaler = pickle.load(open('development/xgboost/scale.pkl', 'rb'))
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


