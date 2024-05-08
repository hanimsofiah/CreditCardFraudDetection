from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
import os

app = Flask(__name__)

try:
    model = pickle.load(open('development/testing/model.pkl', 'rb'))
except Exception as e:
    model = None
    model_loaded = f"Failed to load model: {e}"
else:
    model_loaded = "Model loaded successfully!"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            input_string = request.form['features']
            feature_list = [float(x) for x in input_string.split(',')]

            columns = ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 
                       'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 
                       'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount']

            features_df = pd.DataFrame([feature_list], columns=columns)
            
            prediction = model.predict(features_df)
            result = 'Fraud' if prediction[0] else 'Not Fraud'
            return render_template('index.html', prediction=result, model_loaded=model_loaded)
        except Exception as e:
            return render_template('index.html', prediction=f"Error: {str(e)}", model_loaded=model_loaded)
    else:
        return render_template('index.html', model_loaded=model_loaded)

if __name__ == '__main__':
    app.run(debug=True)
