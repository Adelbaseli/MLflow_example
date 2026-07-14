import mlflow

mlflow.set_experiment("demo experiment")

with mlflow.start_run(run_name="Test artifact"):
 #   mlflow.log_params({"theta_2": "2000"})
    mlflow.log_artifact("lecture_1.py")