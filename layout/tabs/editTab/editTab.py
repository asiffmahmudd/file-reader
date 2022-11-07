import PySimpleGUI as sg
from operations.readFromJSON import readData

#function: Edit tab layout for editing users
def editTab():
    data = readData()
    if len(data) > 0:
        data = processEditData(data)
    return [
        [
            sg.Listbox(
                data, 
                size=(70, 8)
            )
        ]
    ]
    
def processEditData(data): 
    temp = []
    for row in data:
        rowStr = ""
        for val in row.values(): 
            rowStr += str(val) + " "
        temp.append(rowStr)
    return temp