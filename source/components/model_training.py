#this file we used to train the ml model and selecting best model according accuracy score 
#and saving best model file in format of pkl into artifact directory

#importing all the important library which is used for training the model 
import pandas as pd,numpy as np,sklearn
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score,recall_score,precision_score,f1_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from source.exception import CustomException
from source.logger import logging
#this dataset is the case of classifiaction algorithm so we have to perform hyperparameter tuning and set the best hyperparameter and then only get best model and score in it
from sklearn.model_selection import GridSearchCV
from source.utils import Save_object,Evaluate_model
from dataclasses import dataclass #this class we used to define filepath as a class variable
import os,sys


#creating a class to define the filepath to store best modelfile.pkl format into artifacts 
@dataclass
class ModelTrainerConfig():
    #defining the filepath model.pkl to store into artifacts folder
    trained_model_filepath = os.path.join('artifacts','model.pkl')



#creating another class to start the training to the dataset!!!
class ModelTrainer():
    #creating constructor method to initialize the ModelTrainerConfig class variable as object init
    def __init__(self):
        self.trained_model_filepath_obj = ModelTrainerConfig()


    #creating another ModelTrainer method to start training the model in given dataset!!!
    def initiate_model_training(self,train_array,test_array):
        logging.info('Before Training the model By given Dataset first splitt the dataset into training and testing')
        try:
            #splitting the dataset into training and testing
            x_train = train_array[:,:-1]
            y_train = train_array[:,-1]
            logging.info('Training Dataset split into x_train,y_train')
            x_test = test_array[:,:-1]
            y_test = test_array[:,-1]
            logging.info('Testing Dataset split into x_test,y_test')

            #creating a dictatonary of all the model which we want to train
            logging.info('creating a dictatonary of all the model object which we want to train')
            models = {
                'LogisticRegression':LogisticRegression(),
                'DecisionTreeClassifier':DecisionTreeClassifier(),
                'RandomForestTree':RandomForestClassifier(),
                #calling the algorithm of boosting technique
                'AdaBoost':AdaBoostClassifier(),
                'GradientBoosting':GradientBoostingClassifier(),
                'ExtremeGradientBoosting':XGBClassifier(),
                'Svm':SVC()
            }

            #according to the above all classifiction algorithm object we r defining the hyperpaprameter tuning grid for each model
            param_grid = {

                        #for logistic regression algorithm
                        'LogisticRegression':{
                            'penalty':['l1','l2','elasticnet','none'],
                            'random_state':[42],
                            'max_iter':[100,200,500,1000],
                            'solver':['lbfgs','liblinear','sag','saga','newton-cg']
                            },

                        #setting hyperparameter for Decisiontreeclassifier algorithm
                        'DecisionTreeClassifier':{
                            'criterion':['entropy','gini'],
                            'random_state':[42],
                            'max_depth':[2,4,6,8],
                            'min_samples_leaf':[40,50,60,70,80,90,100],
                            'min_samples_split':[2,3,4,5],
                            'max_features':['auto','sqrt','log2',None],
                            'class_weight':['balanced',None]
                        },
                        #setting hyperparameter for RandomForestTree algorithm
                        'RandomForestTree':{
                            'criterion':['entropy','gini'],
                            'random_state':[42],
                            'max_depth':[2,4,6,8],
                            'min_samples_leaf':[40,50,60,70,80,90,100],
                            'min_samples_split':[2,3,4,5],
                            'max_features':['auto','sqrt','log2',None],
                            'class_weight':['balanced',None],
                            'n_estimators':[10,15,20] #[10,20,30,40,50]
                        },
                        #setting hyperparameter for AdaBoost algorithm
                        'AdaBoost':{
                            'random_state':[42],
                            'estimator':[None],
                            'n_estimators':[10,15,20],
                            'learning_rate':[0.1,0.2,0.5,1.0],
                            'algorithm':['SAMME']
                        },
                        #setting hyperparameter for GradientBoosting algorithm
                        'GradientBoosting':{
                            'random_state':[42],
                            'loss':['log_loss','exponential'],
                            'n_estimators':[10,15,20],
                            'learning_rate':[0.1,0.2,0.5,1.0],
                            'max_depth':[2,4,6,8],
                            'min_samples_leaf':[40,50,60,70,80,90,100],
                            'min_samples_split':[2,3,4,5],
                            'max_features':['auto','sqrt','log2',None],
                            'criterion':['friedman_mse','squared_error'],
                            'subsample': [0.8, 1.0]
                        },
                        #setting hyperparameter for SVM algorithm
                        'Svm':{
                            'C':[0.1,0.3,0.5,0.7,0.9],
                            'kernel':['linear','rbf','poly'],
                            'class_weight':['balanced','dict'],
                            'random_state':[42],
                            'degree':[3,4,5],
                            'gamma': ['scale', 'auto']
                        },

                        #now setting the hyperparameter value for XGBclassifier algorithm
                        'ExtremeGradientBoosting':{
                            'n_estimators':[10,15,20],
                            'learning_rate':[0.1,0.2,0.5,1.0],
                            'max_depth':[2,4,6,8],
                            'reg_alpha': [0, 0.5, 1],
                            'reg_lambda' : [0, 0.5, 1],


                        }



            }

            #now passing these model and param_grid to evaluate_model()function to find out best model 
            model_report:dict = Evaluate_model(models = models,param_grid = param_grid,x_train = x_train,y_train = y_train,x_test = x_test,y_test=y_test)

            #now from model_report finding out best model_score and name from it
            best_model_score = max(model_report.values())
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            #now passing the condition if best_model_score >0.85 then only show
            if best_model_score > 0.80:
                logging.info(f"Best model is {best_model_name} and best score is {best_model_score}")
                #now saving the object into artifacts folder
                Save_object(
                    filepath=self.trained_model_filepath_obj.trained_model_filepath,
                    object = models[best_model_name]
                )

            else:
                logging.info('No Best Score Found')


            

            
        except Exception as e:
            raise CustomException(e,sys)