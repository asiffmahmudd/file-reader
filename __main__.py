import PySimpleGUI as sg
from layout.createLayout import createLayout
from operations.addData import addData
from operations.populateInputFields import populateInputFields
from operations.deleteData import deleteData
from operations.updateData import updateData
from operations.clearInputs import clearInputs
import globalStore.globals as globals

selectedIndex = -1
def handleEvents(event, values):
    global selectedIndex
    if event == '-ADD_BTN-':
        addData(values)
    elif event == '-UPDATE_BTN-':
        print(selectedIndex)
        if selectedIndex > -1:
            updateData(selectedIndex)
            sg.popup("Update successful!")
        else:
            sg.popup("No row selected from the table")
        clearInputs()
        selectedIndex = -1
    elif event == '-DELETE_BTN-':
        if selectedIndex > -1:
            deleteData(selectedIndex)
        else:
            sg.popup("No row selected from the table")
        selectedIndex = -1
    elif event == '-INFO_TABLE-':
        try:
            selectedIndex = values['-INFO_TABLE-'][0]
            populateInputFields(globals.info[selectedIndex].values())
        except:
            return
#function: main function. the app starts here
if __name__ == "__main__":    
    layout = createLayout()
    globals.window = sg.Window('File Reader', layout, element_justification='c', size=(1000, 500))
    while True:
        event, globals.values = globals.window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        handleEvents(event, globals.values)
    
    globals.window.close()