import mlflow
import pandas as pd

mlflow.set_experiment("Youtube tutorial")

with mlflow.start_run(run_name="Logging Demo", run_id="6ddf7dc47e394a65b428cb2e50cf982f"):
    #paramters
    #key value
    #dictionary
    mlflow.log_param("learning_rate", 0.03)
    mlflow.log_param("epoch", 100)

    parameters = {
        "learnig_rate_1": 0.04,
        "epoch_1": 200
    }

    mlflow.log_params(parameters)

    mlflow.log_metric("accuracy", "90")

    metrics = {
        "accuracy_1": 80
    }
    mlflow.log_metrics(metrics)

    #artifacts
    artifact_path = "log-1.png"
    mlflow.log_artifact(artifact_path)

    #mlflow.log_image()
    demo_df = pd.DataFrame({"name": ['Adel', 'Ali']})
    mlflow.log_table(demo_df, "demo_df.json")

    titanic_df = pd.read_csv("titanic.csv")
    mlflow.log_table(titanic_df, "titanic_df.json")

    #mlflow.log_assessmnet
    