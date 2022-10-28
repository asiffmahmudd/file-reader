import PySimpleGUI as sg
from layout.createLayout import createLayout
from validation.validation import isValid

#function: main function. the app starts here
if __name__ == "__main__":    
    layout = createLayout()
    window = sg.Window('File Reader', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if isValid(values):
            print("save to csv")
    window.close()
    
