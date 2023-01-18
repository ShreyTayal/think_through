import numpy as np
import pandas as pd


df = pd.read_csv("user_data.csv")

#returns cleaned format of the dataframe, taking out any columns with no data
def clean_data(df):
    df = df.dropna(axis=1, how='all')
    '''df = df.fillna(0)'''
    return df

user_df = clean_data(df)
print(user_df)
