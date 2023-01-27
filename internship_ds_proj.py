import numpy as np
import pandas as pd


df = pd.read_csv('user_data.csv')

#returns cleaned format of the dataframe, taking out any columns with no data

def clean_data(df):
    df = df.dropna(axis=1, how='all')
    
    #make the phone numbers the index collumn and remove duplicate IDs
    df = df.set_index("UserID (Phone Number)")
    df.index.drop_duplicates()
    
    #delete old average row and add an dynamic average row at the end of all the numbers
    df = df.drop(df.index[-1])
    df.loc["Avg"] = np.nan
    df.loc["Avg"] = df.mean(numeric_only=True, axis=0)
    return df

user_df = clean_data(df)

#testing the creation of the y-coordinate of the political quadrant using two of the questions
def create_y(df):
    y = df.loc[:, ['Police Brutality', 'Free Market']]
    y["Averages"] = [np.mean(a=y.loc[item, :]) for item in y.index]
    return y

print(create_y(user_df))
