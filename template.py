import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO , format = '[%(asctime)s]: %(message)s:')
project_name = 'CNN_classifier'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filemame = os.path.split(filepath)

    if filedir !='':
        os.makedirs(filedir , exist_ok = True)
        logging.info("creating directory : {}".format(filedir))
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath , "w") as f :
            pass
            logging.info("creating empty file {}".format(filepath))

    else :
        logging.info("{} already exists ")
        


