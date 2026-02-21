import pandas as pd
import pyodbc

server = r"LAPTOP-Q3G6FU3V\SQLEXPRESS"
database = "irisdata"

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    f"Server={server};"
    f"Database={database};"
    "Trusted_Connection=yes;"
)

query = "SELECT * FROM IRIS"

df = pd.read_sql(query, conn)

print(df.head())