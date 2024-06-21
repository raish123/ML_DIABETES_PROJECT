#this file we used to track the error or custom exception occur during runtime execution of code by interpreters
#and tracked error saving into text file with.log extension and all text file saving into logs directory

#this file we used to track the error or custom exception occur during runtime execution of code by interpreters
#and tracked error saving into text file with.log extension and all text file saving into logs directory

#so importing all the important library which is used to create logging module
import logging
import os,sys
from datetime import datetime



#creating log folder that contain logging file in it
folder_name = 'LOGS'
if not os.path.exists(folder_name):
    os.makedirs(folder_name,exist_ok=True)

#now creating log_file filepath
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") #now and strftime is a built in method of datetime class
filename = f"LOGS_FILE_{timestamp}.log"
log_file_path = os.path.join(folder_name,filename)


#now creating an object of basicConfig class of logging library
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s -%(lineno)d- %(message)s' # Log message format
)