#this file we are writing the code in a such way it provide functionality to my whole application whwnever its needed
from source.logger import logging
from source.exception import CustomException
import os,sys
import numpy as np,dill
#now calling gridsearchcv class here
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score,recall_score,precision_score,f1_score


def Save_object(filepath,object):
    logging.info('Here in Utils we r Creating Save object Function will Save model and preprocessor files to artifacts Folder')
    try:
        logging.info('Now Checking Filepath Exist or not')
        if not os.path.exists('artifacts'):
            os.makedirs('artifacts',exist_ok=True)
        with open(filepath,'wb') as file:
            dill.dump(object,file)
        logging.info('Object Save Into Artfacts Folder')
    except Exception as e:
        raise CustomException(e,sys)


def Evaluate_model(models,param_grid,x_train,y_train,x_test,y_test):
    logging.info('Here in Utils we r Creating Evaluate model Function will Evaluate model and preprocessor files')
    model_report={}
    try:
        #now iterating each model_name and model_obj from models using items() built in method of dict class(its rtn key and value from dictatonary)
        for model_name,model in models.items():
            #creating an object of gridsearch cv to find out according to hyperpaprameter which model is the best for this given dataset
            grid_search = GridSearchCV(estimator=model,param_grid=param_grid[model_name],scoring='accuracy',n_jobs=-1,cv=5)

            #now gridsearch cv fit the model and findout best hyperpaprameters
            grid_search.fit(x_train,y_train)

            logging.info(f"Best model {model_name} and Best hyperpaprameter Value is {grid_search.best_params_}")
            logging.info(f"Best model Score {model_name} is : {grid_search.best_score_}")

            logging.info('Now Setting the Best Hyperpaprameter for each model then doing training and testing the model')
            #now setting the best hyperpaprameter for each model
            model.set_params(**grid_search.best_params_)

            #now training the model by 80% training data
            model.fit(x_train,y_train)

            #now testing the model by 20% test data
            y_pred = model.predict(x_test)

            #now finding the accuracy of each model and storing into model_report according to model_name
            model_report[model_name] = accuracy_score(y_test,y_pred)

        return model_report

    except Exception as e:
        raise CustomException(e,sys)
    
    
#creating userdefined function to unpickle the file
def LoadObject(filepath):
    try:
        with open(filepath,'rb') as file:
            object = dill.load(file)

        return object
    except Exception as e:
        raise CustomException(e,sys)