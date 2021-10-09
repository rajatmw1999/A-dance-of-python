import pandas as pd
import matplotlib.pyplot as plt

titanic_data = pd.DataFrame(
    {
        "name":["Preyansh","Prerit","Doreamon"],
        "age":[11,11,24],
        "type":["Human","Human","Robo Cat"],
        "century":["21st","21st","22nd"],
        "specialPower":["coding","coding","gadgets"]
    }
)

print(titanic_data.plot())