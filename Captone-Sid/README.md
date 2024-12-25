# mlpipeline-example
repo contains an example for working with ml pipelines

#### ML_101
repo contains ML related stuff - docs, codes, datasets, books, PPTs

if using bash terminal  you can create files using touch command
for example, touch template.py and push it on github 


#### create virtual env 
in our base env we have many packages installed so we are using venv

"""
bash :

conda create -n mlrebit python=3.10 -y

#### JFK : -p
conda create -p mlrebit python=3.10 -y
#### when you use -p the env is created within the project structure locally

to activate the venv
conda activate mlrebit

requirement installation command
pip install -r requirements.txt

"""

#### Blog for YAML
https://medium.com/analytics-vidhya/how-to-write-configuration-files-in-your-machine-learning-project-47bc840acc19


#### writing project utility 
logging,exceptions and utils module

why we need logging ? 
Inside src, we have ML rebit folder (this is user defined)
Inside the same we have utils, we have __init__.py (constructor file)
we will use constructor file for logging purposes
OR you can also create another folder for logging purposes.

#### for exception 
we are using box exception 
from box.exceptions import BoxValueError
raising exception with box exception

#### project workflows
#### they need to be updated one after the other
update config.yaml  (artifacts)
update schema.yaml (column : data type)
update params.yaml (all the parameter changes wrt to algo can be done in params.yaml)
update the entity (check this in data_ingestion.ipynb)
update the configuration manager in src config
(Inside src,under config we have configuration.py)
update the components
update the pipeline (flow of function calling)
update the main.py (root file to be triggered for executing training pipeline)
update the app.py (frontend part)


In Data Transformation stage, we do the train test split operation

Steps in pipeline include:
1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Training
5. Model Evaluation
6. Model Deployment
7. Model Monitoring
