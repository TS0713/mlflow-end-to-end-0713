# mlflow-end-to-end-0713
MLFLOW Project End to End

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py

''''
# How to Run ?
''''
### Steps
Clone the respository

```bash
https://github.com/TS0713/mlflow-end-to-end-0713.git
```

```
### STEP 01 - Install Python 3.10 and link the existing virtual environment (mini01) after opening the repository

'''bash

#### cmd
- mlflow ui

#### dagshub
[dagshub](https://dagshub.com/)

import dagshub
dagshub.init(repo_owner='TS0713', repo_name='mlflow-end-to-end-0713', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

  ```bash
  export MLFLOW_TRACKING_URI=https://dagshub.com/TS0713/mlflow-end-to-end-0713.mlflow
  export MLFLOW_TRACKING_USERNAME=TS0713