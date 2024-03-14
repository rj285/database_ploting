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
    
    result_df = pd.DataFrame({
        "DATE":sorted(df['date']),
        "NORMALIZED_PRICE":df['nprice'],
        "STANDERD_DEVIATION":sd_romart
    })
    
    # print(result_df)
    desc = result_df.describe()
    # print(f"THE DESCRIPTION:-  {desc}") 
    '''
        .describe() method in pandas is used to generate descriptive statistics about the DataFrame's numerical columns.
        It provides information such as count, mean, standard deviation, minimum value, 25th percentile, median (50th percentile), 75th percentile, and maximum value.
    '''
    
    percentil_25=np.percentile(result_df['NORMALIZED_PRICE'],25)
    percentil_30 = np.percentile(result_df['NORMALIZED_PRICE'],30)
    percentil_75=np.percentile(result_df['NORMALIZED_PRICE'],75)
    # print(f"25%:- {percentil_25} | 30%:- {percentil_30} | 70%:- {percentil_75}")
    '''
        np.percentile() is a function from the NumPy library that calculates the percentile of a given array or list along a specified axis.
        It allows you to calculate percentiles based on a provided array of data.
    '''

    variance_nprice = np.var(result_df['NORMALIZED_PRICE'])
    print(f"variance:- {variance_nprice}")
    
    '''
        np.var() is a NumPy function used to compute the variance of a dataset.
        Variance is a measure of how much the values in a dataset vary from the mean.
    '''