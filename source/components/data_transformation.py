#this file we used to convert object column to numeric and filling the null value by mean,median,mode using
#simpleimputer class of sklearn
#and preprocessing file saving into pkl format in artifacts folder 
#this preprocessor file we used to do transformation whenever we take input from ui page this preprocessor` file` we gonna used

#importing all the important library we gonna used to perform data transformation
import pandas as pd,numpy as np,sklearn
#below class we used to convert object to numeric
from sklearn.preprocessing import OneHotEncoder,LabelEncoder,StandardScaler
#to fill the null value we have to import simple imputer class 
from sklearn.impute import SimpleImputer
#here we r creating pipeline to perform transformation step by step
from sklearn.pipeline import Pipeline
#to combine all the pipeline together we r using Columntransformer class
from sklearn.compose import ColumnTransformer
#to split the data we r gonna train_test_split class
from sklearn.model_selection import train_test_split
#here we r creating our own custom laberl encoder class we reqd to class transformixin,base estimator class of base sklearn
from sklearn.base import BaseEstimator,TransformerMixin
#now calling logger module class
from source.logger import logging
#now calling file handler class
from source.exception import CustomException 
import os,sys
#now calling the dataclass to define class variable
from dataclasses import dataclass
from source.utils import Save_object

#creating own custom class to perform label encoding
class CustomLabelEncoder(BaseEstimator,TransformerMixin):
    #creatring constructor method -->constructor method run itself automatically whenever we call CustomLabelEncoder class
    def __init__(self):
        pass
    #creating another object method to fit the input  variable only
    def fit(self,x,y=None):
        return self
    
    #creating another object method to convert (input feature)object column to numeric column
    def transform(self,x,y=None):
        #creating empty 2d numpy object as well creating LabelEncoder class object
        x_encoded = np.empty(shape=x.shape,dtype='object')
        le = LabelEncoder()
        #now iterating each object column and performing transformation init and dtoring into 2d numpy array object
        for i in range(x.shape[1]):
            x_encoded[:,i] = le.fit_transform(x_encoded[:,i])
        return x_encoded


#creating class of data_transformation config in which we r defining a class variable to stored our preprocess file into artifacts folder
@dataclass
class DataTransformationConfig():
    preprocessor_filepath = os.path.join('artifacts','preprocessor.pkl')


#creating another class to perform data transformation like filling null converting object to column
class DataTransformation():
    #creating a constructor method to initialise as object variable t5o store DataTransformationConfig class filepath
    def __init__(self):
        self.preprocessor_file_obj = DataTransformationConfig()

    #creating another object method to start initiating the data transformation like filling null converting object to column
    def get_data_transformation(self,raw_data):
        try:
            logging.info('Creating Preprocessor object Through pipeline and ColumnTransformer')
            df =  pd.read_csv(raw_data)
            logging.info('Selecting input and output Variable from Raw Data')
            x = df.drop('Outcome',axis=1) #must be 2d in nature

            logging.info('Selecting categorical and numerical column from input features')
            numerical_feature_colm = x.select_dtypes(exclude='object').columns.to_list()
            categorical_feature_colm = x.select_dtypes(include='object').columns.to_list()

            logging.info('Name Of Categorical Feature Column will be: %s\n',categorical_feature_colm)
            logging.info('Name Of Numerical Feature Column will be: %s\n',numerical_feature_colm)

            #now creating numeric pipeline block of steps
            numeric_pipeline = Pipeline(steps=[
                ('imputer',SimpleImputer(strategy='median')),#filling the null value by median
                ('scaling',StandardScaler(with_mean=False)) #changing all the numeric unit into single unit by doing standard scaling  
                  ])
            logging.info('Numerical Pipeline will be: %s\n',numerical_feature_colm)

            #now creating categorical pipeline first filling null,then convering object to numeric then doing scaling
            categorical_pipeline = Pipeline(steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),#filling null by mode
                ('customlabelencoder',CustomLabelEncoder()),#converting object column to numeric
                ('scaling',StandardScaler(with_mean=False))#changing all the numeric unit into single unit by doing standard scaling  
            ])
            logging.info('Categorical Pipeline will be: %s\n',categorical_pipeline)

            #combining both pipeline using Columntransformer to generator preprocessor object
            #creating an object of Columntransformer class
            preprocessor = ColumnTransformer(transformers=[
                ('categorical_pipeline',categorical_pipeline,categorical_feature_colm),
                ('numerical_pipeline',numeric_pipeline,numerical_feature_colm)
            ])
            logging.info('preprocessor Pipeline will be: %s\n',preprocessor)

            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
        
    #creating another object method to do transformation on training and testing data
    def initate_data_transformation(self,train_path,test_path,raw_path):
        logging.info('Initiating Data Transformation Process')
        try:
            logging.info('Creating training and testing df object using Pandas Library')
            df_train = pd.read_csv(train_path)
            df_test = pd.read_csv(test_path)

            logging.info('Selecting input and output variable from training df object and testing df object')
            target = ['Outcome']
            #Selecting input and output variable from training df object
            train_input_feature = df_train.drop(target,axis=1)
            train_output_feature = df_train[target]

            #Selecting input and output variable from testing df object
            test_input_feature =  df_test.drop(target,axis=1)
            test_output_feature = df_test[target]

            #creating preprocessor_object_variable or attributes
            preprocessor_obj = self.get_data_transformation(raw_data = raw_path)

            #using preprocessor object doing scaling on input features/variable only!!
            numpy_train_input_feature = preprocessor_obj.fit_transform(train_input_feature)
            numpy_test_input_feature = preprocessor_obj.transform(test_input_feature)

            logging.info('Combining training and testing numpy array object with target variable')

            train_array = np.c_[numpy_train_input_feature,np.array(train_output_feature)]
            test_array = np.c_[numpy_test_input_feature,np.array(test_output_feature)]

            logging.info('Now Saving Thre Preprocessor Object to Artifacts Folder')

            Save_object(
                object = preprocessor_obj,
                filepath = self.preprocessor_file_obj.preprocessor_filepath
            )



            return (
                train_array,
                test_array,
                self.preprocessor_file_obj.preprocessor_filepath
            )

        except Exception as e:
            raise CustomException(e,sys)