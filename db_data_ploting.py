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
    id_to_retrieve = input ("enter the ID to retrieve the history: ")
    cursor.execute("SELECT history FROM pis_tb WHERE id = %s",(id_to_retrieve,))
    
    result =cursor.fetchone()
    history_json = result[0]
    history_list = json.loads(history_json)
    df = pd.DataFrame(history_list)
    # for i in history_list:
    #     price = i['nprice']
    #     print(price)
    date = df['date']
    nprice = df['nprice']
    n_price=pd.to_numeric(list(nprice))
    # print(f"average:{sum(n_price)/len(n_price)}")
    # print(n_price)

    x = np.array(sorted(date))
    y = np.array(sorted(pd.to_numeric(nprice)))
    plt.plot(x,y,marker = '+')
    plt.title('HISTORY OF N_PRICE')
    plt.xlabel('DATE')
    plt.ylabel('N_PRICE')
    plt.savefig("1_db_data_ploting.png")
    plt.show()