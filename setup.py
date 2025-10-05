from setuptools import find_packages, setup
from typing import List
import os
def get_requirements() -> List[str]:
    
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Acash Tech",
    author_email="acashtech28@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
    include_package_data=True,
    description="A FastAPI-based data ingestion and ML pipeline with MongoDB integration",
    long_description=open('README.md').read() if os.path.exists('README.md') else "",
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
