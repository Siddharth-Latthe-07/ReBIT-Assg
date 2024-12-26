# Capstone Project
repo contains an end-to-end project for working with ml pipelines




#### 1. Create virtual env 
in our base env we have many packages installed so we are using venv


#### 2. Install req.txt
```
pip install -r requirements.txt
```

#### 3. Writing project utility 
logging,exceptions and utils module




#### 4. Project workflows:- They need to be updated one after the other
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
