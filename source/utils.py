#this file we are writing the code in a such way it provide functionality to my whole application whwnever its needed
from source.logger import logging
from source.exception import CustomException
import os,sys
from dotenv import load_dotenv
import pymysql
import pandas as pd
#loading the important parameter which is present in dotenv class by creating load_env object
load_dotenv()

db_name = os.getenv('database_name')
db_username = os.getenv('database_username')
db_port = os.getenv('database_port')
db_host = os.getenv('database_host')
db_pass = os.getenv('database_password')

#now creating user defined function to read the structured data from database and return as df object
def read_sql_data():
    logging.info('Reading The Data From SQL Server')
    try:
        logging.info('Using PYMysql Connector for connecting MYSQL Database through Python')
        conn = pymysql.connect(
            host=db_host,
            user=db_username,
            password=db_pass,
            db=db_name,
            port = int(db_port)
        )
        logging.info('Database Connected Successfully')
        cur = conn.cursor()
        logging.info('Storing the Database Table into DF object Using Pandas')
        df = pd.read_sql_query('select * from kaggle_diabetes',conn)

        return df 
    
    except Exception as e:
        raise CustomException(e,sys)




