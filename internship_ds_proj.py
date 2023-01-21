import numpy as np
import pandas as pd


df = pd.read_csv("user_data.csv")

#returns cleaned format of the dataframe, taking out any columns with no data
def clean_data(df):
    df = df.dropna(axis=1, how='all')
    '''df = df.fillna(0)'''
    return df

user_df = clean_data(df)

#make the phone numbers the index collumn and remove duplicate IDs
user_df = user_df.set_index("UserID (Phone Number)")
user_df = user_df.drop_duplicates()

#delete old average row and add an dynamic average row at the end of all the numbers
user_df = user_df.drop(user_df.index[-1])
user_df.loc["Avg"] = np.nan
user_df.loc["Avg"] = user_df.mean(numeric_only=True, axis=0)



print(user_df)
