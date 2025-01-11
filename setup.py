from setuptools import setup,find_packages
from typing import List

HYPEN_DOT = "-e ."

def get_requirement(file_path:str):
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("/n","") for req in requirements ]
        
        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)
    return requirements

setup(
    name ="ml project",
    version="0.0.1",
    author="sandeep",
    packages=find_packages(),
    install_requires= get_requirement("requirements.txt")
    
)