from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements




Hyphen_e_dot='-e .'
setup(
    Name = "Machine Learning Project",
    version = '0.0.1',
    author = 'D.N.Raghavendra',
    author_email = 'dosinarayanaraghavendra@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
    
    
)
if Hyphen_e_dot in requirements:
    requirements.remove(Hyphen_e_dot)