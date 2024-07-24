#this file we used to create prediction pipeline for my model!!!
#in this file we first change new datapoint to df object then do transformation and scaling to nrew datapoint then will do prediction of new datapoint
#importing all the important library which is used to create the prediction pipeline
import pandas as pd,numpy as np
import os,sys
from source.exception import CustomException
from source.logger import logging
import sklearn,dill #dill classwe used to unpickle the model and transformation file
from source.utils import LoadObject


#creating a class of Predict to perform user enter data to do transformation and also to do prediction!!!
class PredictModel():
    #creating empty constructor method 
    def __init__(self):
        pass

    #creating another method to do prediction of datapoint
    def Predict(self,feature):
        try:
            logging.info('Now unpickling the model and preprocessing file')
            #path of model and preprocessing file
            filepath_model = r'artifacts\model.pkl'
            filepath_preprocessing = r'artifacts\preprocessor.pkl'
            #calling the load object function and passing parameter in it
            preprocessor_obj = LoadObject(filepath_preprocessing)
            model_obj = LoadObject(filepath_model)

            #Now Doing Transformation of New Datapoint
            transformation = preprocessor_obj.transform(feature)
            logging.info('Doing Transformation of New Datapoint%s\n',transformation)

            #Now Doing prediction on New datapoint
            pred = model_obj.predict(transformation)
            return pred
          
        except  Exception as e:
            raise CustomException(e,sys)
        


#creating a class to convert new datapoint to df object 
class CustomData():
    #creating constructor method to initialize the object variable in it
    def __init__(self,Pregnancies:int,Glucose:int,BloodPressure:int,SkinThickness:int,Insulin:int,BMI:float,DiabetesPedigreeFunction:float,Age:int):
        self.Pregnancies = Pregnancies
        self.Glucose = Glucose
        self.BloodPressure = BloodPressure
        self.SkinThickness = SkinThickness
        self.Insulin = Insulin
        self.BMI = BMI
        self.DiabetesPedigreeFunction = DiabetesPedigreeFunction
        self.Age = Age

    #creating another CustomData Class method to convert the new datapoint to df object
    def Dataframe(self):
        try:
            logging.info('Convert the New Datapoint to DF object')
            #creating a dictionary of new datapoint
            data = {'Pregnancies':[self.Pregnancies],
                    'Glucose':[self.Glucose],
                    'BloodPressure':[self.BloodPressure],
                    'SkinThickness':[self.SkinThickness],
                    'Insulin':[self.Insulin],
                    'BMI':[self.BMI],
                    'DiabetesPedigreeFunction':[self.DiabetesPedigreeFunction],
                    'Age':[self.Age]
                    }
            

            feature = pd.DataFrame(data)
            logging.info('New Datapoint Convert to Dataframe%s\n',feature)

            return feature


        except Exception as e:
            raise CustomException(e,sys)



    