from operations.clearInputs import clearInputs
from operations.writeToJSON import writeToJSON
from validation.validation import isValid
from operations.updateTableData import updateTableData
import globalStore.globals as globals

def addData(values):
    if isValid(values):
        data = {}
        data["name"] = values["-NAME-"]
        data["salary"] = values["-SALARY-"]
        data["birthday"] = values["-BIRTHDAY-"]
        writeToJSON(data)
        clearInputs()#list(values.keys())[:len(data.keys())])
        globals.info.append(data)
        updateTableData()
