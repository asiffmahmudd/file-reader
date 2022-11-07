import json
import os
  

def readData():
    try:
        filePath = os.path.join(os.path.dirname(__file__), "../data/userdata.json")
        # Opening JSON file
        f = open(filePath)
        
        # returns JSON object as 
        # a dictionary
        data = json.load(f)

        # Closing file
        f.close()

        return data['info']
    except:
        return []
