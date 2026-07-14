import mlflow

model_url = "models:/best-production-model/3"
mlflow_model = mlflow.sklearn.load_model(model_url)
print(mlflow_model)