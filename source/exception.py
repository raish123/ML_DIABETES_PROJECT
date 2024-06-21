#this file we used whenever we got exception occur during runtime execution of code dont stop 
#the code just display custom message to output and move futhur execution in code

#importing all the important library which is used to create custom exception class
from source import logger
import os,sys

def custom_error_message(error_message,error_detail:sys):
    #sys module will have all details about error!!!!
     # exc_info() built in method of sys module generally we used to get information of error_details rtn 3 paramter of tuple-->type,error_value,info_error
    _,_,error_tb  = error_detail.exc_info()
    filename = error_tb.tb_frame.f_code.co_filename
    lineno = error_tb.tb_lineno

    message  = f" Python Error getting in the filename {filename} at this line number {lineno} and message of error will be {str(error_message)}"
    
    return message



#creating a custom  exception class will inherit all property from exception
class CustomException(Exception):
    #now creating constructor method to initialized the attribute in it
    def __init__(self,error_message,error_detail:sys):
        #error message we r inheriting parent class Exception se!!!
        super().__init__(error_message)
        self.message = custom_error_message(error_message=error_message,error_detail=error_detail)


    #now displaying this custom message to output by using __str__ method 
    #is a special method generally used to represent string represnetation of object
    def __str__(self):
        return self.message


