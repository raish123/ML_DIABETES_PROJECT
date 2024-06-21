#Once our model is created the setup.py file futhur we used to create  a package and that package can be shared to python community
#so importing all the important library which is used to create setup.py file
from setuptools import setup,find_packages
from typing import List

#creating user defined function to get Get_Requirements
def Get_Requirements(filepath:str)->list[str]:
    requirement = []
    with open(filepath,'r') as file:
        rows = file.read().split('\n')
        for row in rows:
            if '-e .' in row:
                continue
            else:
                requirement.append(row)
    return requirement



#creating an object of setup class of setuptools library
setup(
    name = 'ML_DIABETES_PROJECT',
    version = '0.0.1',
    long_description= open('readme.md','r').read(),
    author='Raees Azam Shaikh',
    author_email='shaikhraishazam@gmail.com',
    url = 'https://github.com/raish123/ML_DIABETES_PROJECT/',
    #creating an object of find_packages class of setuptools library
    packages=find_packages(), #this class is responsible to install all the library which is present in requirements.txt file
    install_requires= Get_Requirements('requirements.txt'), #will be list of libraries


)