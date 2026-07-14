import sqlite3
import pandas as pd

connection = sqlite3.connect("mlflow.db")
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type = 'table';", connection)
runs_df = pd.read_sql_query("SELECT * FROM runs;", connection)
print(runs_df)