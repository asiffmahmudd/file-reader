import PySimpleGUI as sg
from layout.createLayout import createLayout
from operations.clearInputs import clearInputs
from operations.writeToCSV import writeToCSV
from validation.validation import isValid

lastId = 0

def processData(values, window):
    global lastId
    if isValid(values):
        data = {}
        data["id"] = lastId + 1
        lastId += 1
        data["name"] = values["-NAME-"]
        data["salary"] = values["-SALARY-"]
        data["birthday"] = values["-BIRTHDAY-"]
        writeToCSV(data)
        clearInputs(window, list(values.keys())[:len(data.keys())-1])

#function: main function. the app starts here
if __name__ == "__main__":    
    layout = createLayout()
    window = sg.Window('File Reader', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        processData(values, window)
    window.close()
    
