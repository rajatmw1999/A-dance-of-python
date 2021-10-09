import pandas as pd

# creating a data frame 
titanic_data = pd.DataFrame(
    {
        "name":["Preyansh","Prerit","Doreamon"],
        "age":[11,11,24],
        "type":["Human","Human","Robo Cat"],
        "century":["21st","21st","22nd"],
        "specialPower":["coding","coding","gadgets"]
    }
)

# print(titanic_data.describe())

# selecting a series 
print(titanic_data["age"].max())

# creating a series 
titanic_series = pd.Series(["Preyansh","Prerit","Nobita"], name="Boyz")
print(titanic_series)


# REMEMBER

# Import the package, aka import pandas as pd

# A table of data is stored as a pandas DataFrame

# Each column in a DataFrame is a Series

# You can do things by applying a method to a DataFrame or Series

# https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html