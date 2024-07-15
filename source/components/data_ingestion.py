#data_ingestion file means we r reading the data from differnet source can be database server,cloud server ...so on
#after reading the data from source biffurgating the train ,test,raw data and saving those data into artifacts folder
import pandas as pd
from source.exception import CustomException
from source.logger import logging
import os,sys
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass #this class we used define as class variable using decorator function


#now creating a data_ingestion config class in which we r defining path of train,test,raw data which is used as class variable 
@dataclass
class DataIngestionConfig():
    #here we r defining the filepath of data as class variable
    raw_data_filepath = os.path.join('artifacts','raw.csv')
    train_data_filepath = os.path.join('artifacts','train.csv')
    test_data_filepath  = os.path.join('artifacts','test.csv')


#now creating another class DataIngestion to read the data from source and bifurgate into train,test,raw data
class DataIngestion():
    #creating constructor method and initializing attribute class variable from DataIngestionConfig class wheenever we create DataIngestion class object constructor automatically run itself
    def __init__(self):
        self.data_ingestion_obj = DataIngestionConfig()

    #creating another object method to initiate the dataingestion prtocess
    def initiate_data_ingestion(self):
        try:
            logging.info('Initiate the Data Ingestion Process')
            #calling the read_sql_data function and storing the return file in it
            df = pd.read_csv(r'artifacts\raw.csv')
            logging.info('Data Read SuccessFully From Database\n%s',df.head())

            logging.info('Now creating artifact folder and storing raw,train,test data')

            foldername = os.path.dirname(self.data_ingestion_obj.raw_data_filepath)
            os.makedirs(foldername,exist_ok=True)
            df.to_csv(self.data_ingestion_obj.raw_data_filepath,index=False,header=True)
            logging.info('Raw data Save into Artifacts Folder')

            logging.info('Splitting the Raw Data into Train and Test Dataset')
            train_df,test_df = train_test_split(df,test_size=0.2,random_state=42)
            train_df.to_csv(self.data_ingestion_obj.train_data_filepath,index=False,header=True)
            test_df.to_csv(self.data_ingestion_obj.test_data_filepath,index=False,header=True)
            logging.info('Train and Test Dataset Stored into artifacts folder')

            return(
                self.data_ingestion_obj.raw_data_filepath,
                self.data_ingestion_obj.train_data_filepath,
                self.data_ingestion_obj.test_data_filepath
            )

        except Exception as e:
            raise CustomException(e,sys)