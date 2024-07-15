#this file we are writing the code in a such way it provide functionality to my whole application whwnever its needed
from source.logger import logging
from source.exception import CustomException
import os,sys
import numpy as np,dill



def Save_object(filepath,object):
    logging.info('Here in Utils we r Creating Save object Function will Save model and preprocessor files to artifacts Folder')
    try:
        logging.info('Now Checking Filepath Exist or not')
        if not os.path.exists(filepath):
            os.makedirs(filepath,exist_ok=True)
        with open(filepath,'wb') as file:
            dill.dump(object,file)
        logging.info('Object Save Into Artfacts Folder')
    except Exception as e:
        raise CustomException(e,sys)


