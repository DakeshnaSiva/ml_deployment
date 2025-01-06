from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    require = []
    with open(file_path, "r") as file:
        require = file.read().splitlines()
        require = [read.replace("\n", "") for read in require]

    hypen_dor = "-e ."
    if hypen_dor in require:
        require.remove(hypen_dor)
    
    return require


setup(
    name="my_package",
    version="0.0.1",
    author="Dakeshna",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
