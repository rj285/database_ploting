import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd
import numpy as np
import json

connect = mysql.connector.connect(
    host="localhost",
    user="romart_user",
    password="romartuser",
    database="romart_db"
)

cursor = connect.cursor()

while True:
    id_to_retrieve = input ("Enter the ID to retrieve the history: ")
    cursor.execute("SELECT history FROM pis_tb WHERE id = %s",(id_to_retrieve,))
    
    result = cursor.fetchone()
    if result is None:
        print("No data found for the given ID.")
        continue
    
    history_json= result[0]
    history_list = json.loads(history_json)
    df = pd.DataFrame(history_list)
    df['nprice'] = pd.to_numeric(df['nprice'])
    
    mean_price = df['nprice'].mean()
    # print(mean_price)
    
    sd_romart = []
    
    for price in df['nprice']:
        standerd = abs(mean_price-price)
        sd_romart.append(standerd) 
    # print(sd_romart) 
    
    x = df['nprice']
    plt.scatter(x, [mean_price] * len(df), color = 'red', label = f"MEAN PRICE: {mean_price}")
    plt.scatter(x, x, color = 'orange', label = 'nprice')
    plt.xlabel("NORMALIZED PRICE")
    plt.ylabel("MEAN PRICE")
    plt.grid()
    plt.legend()
    plt.show()
    plt.savefig("1_correlation-nprice_meanprice.png")