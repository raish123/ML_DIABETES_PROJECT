# Importing all the necessary libraries used in this file
from flask import Flask, render_template, redirect, url_for, request
from flask_login import current_user
from source.pipelines.predict_pipeline import PredictModel, CustomData
from source.exception import CustomException
from source.logger import logging
import os,sys

# Creating an object of the Flask class
app = Flask(__name__, template_folder='templates', static_folder='static')

# Creating a secret key to maintain the session for the user
app.secret_key = 'thisissecretkeyforsession'


# Creating a route to show the index webpage
@app.route('/')
def index():
    return render_template('home.html')

# Creating route for prediction page using along with decorator function
@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    try:
        # Checking what will be the method of request 
        if request.method == 'POST':
            # Fetching the data from form
            pregnancy = request.form.get('pregnancies')
            glucose = request.form.get('glucose')
            bloodpressure = request.form.get('bp')
            skinthickness = request.form.get('skinthickness')
            insulin = request.form.get('insulin')
            bmi = request.form.get('bmi')
            dpf = request.form.get('dpf')
            age = request.form.get('age')

            # Creating an object of CustomData class
            cd = CustomData(Pregnancies=pregnancy, Glucose=glucose, BloodPressure=bloodpressure,
                            SkinThickness=skinthickness, Insulin=insulin, BMI=bmi,
                            DiabetesPedigreeFunction=dpf, Age=age)

            # Calling Custom data class method Dataframe
            df = cd.Dataframe()

            # Calling the PredictModel class of predict_pipeline module
            pm = PredictModel()

            # Calling PredictModel class method Predict
            result = pm.Predict(feature=df)

            return render_template('result.html', result=result[0])

        msg = "To Reach to Prediction Page...Login Required "
        return render_template('predict.html', msg=msg)
    except Exception as e:
        raise CustomException(e,sys)
        

# Creating route for result
@app.route('/result', methods=['GET', 'POST'])
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
