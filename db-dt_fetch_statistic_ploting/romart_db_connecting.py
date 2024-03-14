import mysql.connector
import json
import pandas as pd

# Establish connection to MySQL
connect = mysql.connector.connect(
    host="localhost",
    user="romart_user",
    password="romartuser",
    database="romart_db"
)

cursor = connect.cursor()

# Read data from CSV
data = pd.read_csv("data.csv")

# Convert 'history' column to JSON
data['history'] = data['history'].apply(eval)
data['history'] = data['history'].apply(json.dumps)

# Iterate through rows and insert into MySQL
for _, row in data.iterrows():
    query = "INSERT INTO pis_tb (id, name, price, history) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (row['id'], row['name'], row['price'], row['history']))

# Commit changes and close connection
connect.commit()
connect.close()
