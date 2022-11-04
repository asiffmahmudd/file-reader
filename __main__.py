import PySimpleGUI as sg
from layout.createLayout import createLayout
from operations.clearInputs import clearInputs
from operations.writeToJSON import writeToJSON
from validation.validation import isValid

lastId = 0

def addData(values, window):
    global lastId
    if isValid(values):
        data = {}
        data["id"] = lastId + 1
        lastId += 1
        data["name"] = values["-NAME-"]
        data["salary"] = values["-SALARY-"]
        data["birthday"] = values["-BIRTHDAY-"]
        writeToJSON(data)
        clearInputs(window, list(values.keys())[:len(data.keys())-1])

def handleEvents(window, event, values):
    if event == '-ACTION_BTN-' and window[event].get_text() == 'Add':
        addData(values, window)
    elif event == '-ACTION_BTN-' and window[event].get_text() == 'Edit':
        print("edit")
    elif event == '-ACTION_BTN-' and window[event].get_text() == 'Delete':
        print("delete")

    elif values[event] == '-CREATE_TAB-':
        window['-ACTION_BTN-'].update('Add')
    elif values[event] == '-EDIT_TAB-':
        window['-ACTION_BTN-'].update('Edit')
    elif values[event] == '-DELETE_TAB-':
        window['-ACTION_BTN-'].update('Delete')


#function: main function. the app starts here
if __name__ == "__main__":    
    layout = createLayout()
    window = sg.Window('File Reader', layout, element_justification='c', size=(1000, 500))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        handleEvents(window, event, values)
    
    window.close()