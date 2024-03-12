import mysql.connector
import json
import pandas as pd


connect = mysql.connector.connect(
    host="localhost",
    user="romart_database",
    password="romart1234",
    database="romart_db"
)

cursor = connect.cursor()

data = pd.read_csv("data.csv")
    # print(data)
data['history'] = data['history'].apply(eval)
    # print(data['history'])
data['history'] = data['history'].apply(json.dumps)
    # print(data['history'])
for _, row in data.iterrows():
    cursor.execute("INSERT INTO pis_tb (id, name, price, history) VALUES (%s, %s, %s, %s)", tuple(row))
connect.commit()
connect.close()