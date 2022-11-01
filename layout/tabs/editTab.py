import PySimpleGUI as sg
from operations.readFromCSV import readData

#function: Edit tab layout for editing users
def editTab():
    data = readData()
    data = processEditData(data)
    edit_tab = [[sg.Listbox(values=[x for x in data], size=(70, 8))]]
    return edit_tab

def processEditData(data): 
    temp = []
    for x in data:
        row = ""
        for y in x.values():
            row += str(y) + " "
        temp.append(row)
    return temp