from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e ."

def get_requirements(file_path:str)->List[str]:
    with open(file_path) as file_path: 
         requirements=[]
         requirements=file_path.readlines()
         requirements=[req.replace("\n"," ") for req in requirements]


         if HYPEN_E_DOT in requirements:
             requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
    name="End_to_End pipeline setup",
    version="0.0.1",author="Devendra",
    author_email="devendrasingh8398@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
