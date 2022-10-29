from setuptools import find_packages, setup
from typing import List
 
'''
This function will return list of reqirements

'''
def get_requirements()-> List[str]:
    requirements_list: List[str] = []
    return requirements_list

    """
    Write a code to read requiremments.txt file and append each reqiurements in requiremntes_list variable.
    
    """

    
setup (
    name="sensor",
    version="0.0.1",
    authoer="Dhruv Saxena",
    author_email="saxena25dhruv@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements() #["pymongo==4.2.0"],
)