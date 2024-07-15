#this file we are creating for testing the code is it working properly or not!!
# so calling the module
from src.logger import logging
from src.exception import CustomException
import os,sys
from source.components.data_ingestion import DataIngestion,DataIngestionConfig
from source.components.data_transformation import DataTransformation,DataTransformationConfig

def main():
    try:
       #creating an object of DataIngestion class
       di = DataIngestion()
       raw_path,train_path,test_path = di.initiate_data_ingestion()

       #creating Datatransformation class object
       dt = DataTransformation()
       

       train_array,test_array,_ = dt.initate_data_transformation(train_path=train_path,test_path=test_path,raw_path=raw_path)

       

    except Exception as e:
        raise CustomException(e,sys)



if __name__ == '__main__':
    main()