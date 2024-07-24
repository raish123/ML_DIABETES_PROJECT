# In this application.py file, we define the routes (mapping URL with specific function) 
# and also bind the Flask application with LoginManager and SQLAlchemy ORM.

# Importing all the necessary libraries used in this file
from flask import Flask, render_template, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from source.pipelines.predict_pipeline import PredictModel,CustomData

# Creating an object of the Flask class
app = Flask(__name__, template_folder='templates', static_folder='static')

# Creating a secret key to maintain the session for the user
app.secret_key = 'thisissecretkeyforsession'

# Creating a route to show the index webpage
@app.route('/')
def index():
    return render_template('home.html')



# Creating route for prediction page using along with decorator function
@app.route('/prediction',methods=['GET','POST'])
def prediction():
    #now checking what will be the method of request 
    if request.method=='POST':
        #now fetching the data from form
        pregnancy = request.form.get('pregnancies')
        glucose = request.form.get('glucose')
        bloodpressure = request.form.get('bp')
        skinthickness = request.form.get('skinthickness')
        insulin = request.form.get('insulin')
        bmi = request.form.get('bmi')
        dpf = request.form.get('dpf')
        age = request.form.get('age')

        #now this fetched data now we have to send to the prediction pipeline before that we have to change new datapoint to df object then 
        #to do transformation and get prediction accuracy and then display accuracy to web application
        
        #creating an object of CustomData class
        cd = CustomData(Pregnancies=pregnancy,Glucose=glucose,BloodPressure=bloodpressure,
                        SkinThickness=skinthickness,Insulin=insulin,BMI=bmi,
                        DiabetesPedigreeFunction=dpf,Age=age)
        
        #now calling Custom data class class built in method Dataframe
        df = cd.Dataframe()

        #now calling the PredictModel class of predict_pipeline module!!!
        pm = PredictModel()

        #now calling PredictModel class built in method Predict
        result = pm.Predict(feature=df)


        return render_template('result.html',result=result[0])

    msg = "To Reach to Prediction Page...Login Required "
    return render_template('predict.html',msg=msg)





if __name__ == '__main__':
    app.run(debug=True)
