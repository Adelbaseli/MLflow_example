import mlflow

mlflow.set_experiment("nested run demo")
with mlflow.start_run(run_name="parent run", nested=True) as parent_run:
    print(f"Parent run: {parent_run.info.run_id}")
    mlflow.log_param("theta", "100")
    with mlflow.start_run(run_name="Child run 1", nested=True) as child_run_1:
        print(f"Child run: {child_run_1.info.run_id}")
    with mlflow.start_run(run_name="Child run 2", nested=True) as child_run_2:
        print(f"Child run: {child_run_2.info.run_id}")
    with mlflow.start_run(run_name="Child run 3", nested=True) as child_run_3:
        print(f"Child run: {child_run_3.info.run_id}")