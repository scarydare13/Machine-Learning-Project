from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements from a file.
    It removes the '-e .' entry if present.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Read all lines
        requirements = [req.strip() for req in requirements]  # Remove whitespace and newlines

    # Remove the '-e .' entry if present
    if '-e .' in requirements:
        requirements.remove('-e .')

    return requirements

setup(
    name='mlproject',
    version='0.1.0',
    author='godgamer',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
