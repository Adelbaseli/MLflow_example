import mlflow

mlflow.set_experiment("demo experiment")

with mlflow.start_run(run_name="My beautiful run"):
    mlflow.log_params({"theta_2": "2000"})
