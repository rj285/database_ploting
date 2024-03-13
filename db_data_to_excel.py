import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd
import numpy as np
import statistics
import json


connect = mysql.connector.connect(
    host="localhost",
    user="romart_database",
    password="romart1234",
    database="romart_db"
)

cursor = connect.cursor()

while True:
    id_to_retrieve = input ("Enter the ID to retrieve the history: ")
    cursor.execute("SELECT history, name, price FROM pis_tb WHERE id = %s",(id_to_retrieve,))
    
    result = cursor.fetchone()
    if result is None:
        print("No data found for the given ID.")
        continue

    history_json, name, price = result
    history_list = json.loads(history_json)
    df = pd.DataFrame(history_list)
    
    df['nprice'] = pd.to_numeric(df['nprice'])
    
    # mean_price = sum(npricez) / len(npricez)
    # median = statistics.median(npricez)
    # mode = statistics.mode(npricez)
    # sd = np.std(npricez)
    
    mean_price = df['nprice'].mean()
    
    sd_romart = []
    
    for price in df['nprice']:
        standerd = abs(mean_price-price)
        sd_romart.append(standerd)
    print(sd_romart)


    result_df = pd.DataFrame({
        "NAME": [name] * len(df['date']),
        "PRICE":[price] * len(df['date']),
        "DATE":sorted(df['date']),
        "NORMALIZED_PRICE":df['nprice'],
        "STANDERD_DEVIATION":sd_romart
    })
    
    filename = "1_db_data_to_excel.xlsx"
    result_df.to_excel(filename,sheet_name="Sheet1", index=False)
    print(f"DATA SAVED SUCCESSFULLY TO {filename} Sheet1")
    
    