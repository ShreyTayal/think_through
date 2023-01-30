import numpy as np
import pandas as pd

df = pd.read_excel('/Users/akshatchavan/Library/Containers/com.microsoft.Excel/Data/Downloads/(Ketriel Comments) version of _Copy of Master ThinkThrough 23andMe_.xlsx')


# returns cleaned format of the dataframe, taking out any columns with no data

def clean_data(df):
    df = df.dropna(axis=1, how='all')

    # make the phone numbers the index collumn and remove duplicate IDs
    df = df.set_index("UserID (Phone Number)")
    df.index.drop_duplicates()

    # delete old average row and add an dynamic average row at the end of all the numbers
    df = df.drop(df.index[-1])
    df.loc["Avg"] = np.nan
    df.loc["Avg"] = df.mean(numeric_only=True, axis=0)
    return df


user_df = clean_data(df)


# testing the creation of the y-coordinate averages of each user of the political quadrant using two of the questions
def create_y(df):
    y = df.loc[:, ['Police Brutality', 'Free Market']]
    y["Y Averages"] = [np.mean(a=y.loc[item, :]) for item in y.index]
    return y

# testing the creation of the x-coordinate averages of each user of the political quadrant using two of the questions
def create_x(df):
    x = df.loc[:, ["Worker's Rights", "Women's Rights"]]
    x["X Averages"] = [np.mean(a=x.loc[item, :]) for item in x.index]
    return x

x = create_x(df)
y = create_y(df)
#add to the main dataframe, drop duplicate collumns
new_df = pd.concat([x, y], axis=1)

# iterate over the rows of the DataFrame, and return coordinates
for index, row in new_df.iterrows():
    xval = row["X Averages"]
    yval = row["Y Averages"]
    print((xval,yval))






