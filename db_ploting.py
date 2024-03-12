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
    id_to_retrieve = input ("enter the ID to retrieve the history: ")
    cursor.execute("SELECT history FROM pis_tb WHERE id = %s",(id_to_retrieve,))
    
    result =cursor.fetchone()
    history_json = result[0]
    history_list = json.loads(history_json)
    df = pd.DataFrame(history_list)
    date = df['date']
    nprice = df['nprice']
    npricez=pd.to_numeric(df['nprice'])
    
    mean_price = sum(npricez) / len(npricez)
    median = statistics.median(npricez)
    mode = statistics.mode(npricez)
    std = np.std(npricez)
    
    x = np.array(sorted(date))
    y = np.array(sorted(pd.to_numeric(nprice)))
    
    # print(f"MEAN : {mean_price}") 
    # print(f"MEDIAN : {median}") 
    # print(f"MODE : {mode}")
    # print(f"MODE : {type(mode)}")  
    
    plt.plot(x,y,marker = 'o')
    plt.axhline(y=mean_price, color='r', linestyle='--', label=f"mean_price: {mean_price}")
    plt.axhline(y=mode, color='b', linestyle='--', label=f"mode: {mode}")
    plt.axhline(y=median, color='y', linestyle='--', label=f"median: {median}")
    plt.axhline(y=std, color='g', linestyle='--', label=f"standerd deviation: {std}")
    
    plt.title("MEAN / MEDIAN / MODE / STD")
    plt.xlabel("DATES")
    plt.ylabel("NORMALIZED PRICE")
    plt.legend()
    plt.savefig("4_db_ploting.png")
    plt.show()

    
      