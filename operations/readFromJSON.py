import json
import os
import globalStore.globals as info

def readData():
    try:
        filePath = os.path.join(os.path.dirname(__file__), "../data/userdata.json")
        # Opening JSON file
        f = open(filePath)
        
        # returns JSON object as 
        # a dictionary
        jsondata = json.load(f)
        # Closing file
        f.close()

        info.info = jsondata['info']
        return jsondata['info']
    except:
        return []
