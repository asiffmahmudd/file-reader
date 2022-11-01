import pandas as pd
import os

#returns a list of dictionary which were read from the csv
def readData():
    try:
        df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../data/userdata.csv"))
        return df.to_dict('records')
    except:
        return