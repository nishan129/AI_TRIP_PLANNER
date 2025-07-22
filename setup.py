from setuptools import setup,find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """
    requirements_list:List[str] = []
    
    try:
        # Open and read the requirements.txt file
        with open("requirements.txt",'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                # Strip whitespace and newline characters
                requirements= line.strip()
                # Ingnore_empty lines and -e.
                if requirements and requirements != "-e .":
                    requirements_list.append(requirements)
                    
    except FileNotFoundError:
        print("requirements.txt file not found.")
        
    return requirements_list

print(get_requirements())
setup(
    name="AI-TRIP_PLANNER",
    version="0.0.1",
    author="Nishant Borkar",
    author_email="nishantborkar139@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements()
)