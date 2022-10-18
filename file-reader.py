import PySimpleGUI as sg

#funciton: checking if the value is an integer
def isInteger(value):
    try:
        #trying to convert the value into an int and return the value
        value = int(value) 
        return value
    except:
        #if the conversion fails, return false
        return False

#function: checking if the value is positive 
def isPositive(value):
    return value >= 0

#function: checking if name is valid or not
def isNameValid(name):
    errorFlag = 0
    errorMsg = ""
    if name == "":
        errorFlag = 1
        errorMsg = "Name cannot be null. "
    if not name.isAlpha():
        errorFlag = 1
        errorMsg += "Name should only contain alphabets"
    return [errorFlag, errorMsg]

#function: checking if age is valid or not
def isAgeValid(age):
    errorFlag = 0
    errorMsg = ""
    if not isInteger(age):
        errorFlag = 1
        errorMsg = "Age should contain an integer value. "
    if not isPositive(age):
        errorFlag = 1
        errorMsg += "Age should be a positive value"
    return [errorFlag, errorMsg]

#function: validate inputs for users
def validateInput(values):
    name = values["name"]
    age = values["age"]
    birthday = values["birthday"]

#function: Create tab layout for adding users
def createTab():
    create_tab = [  
        [sg.Text("Name:", size=(6,0)), sg.Input("", pad=(10,10), key='name')], 
        [sg.Text("Age:", size=(6,0)), sg.Input("", pad=(10,10), key='age')], 
        [sg.Text("Birthday:", size=(6,0)), sg.Input("", pad=(10,10), key='birthday')],
        [sg.Stretch(),sg.Button('Add', size=(8,1)), sg.Button('Cancel', pad=(10,5), size=(8,1))]
    ]
    return create_tab

#function: Edit tab layout for editing users
def editTab():
    edit_tab = [[sg.T("edit tab")]]
    return edit_tab

#function: delete tab layout for deleting users
def deleteTab():
    delete_tab = [[sg.T("Delete tab")]]
    return delete_tab

#function: adding all the tabs together and creating the window layout for the app
def createLayout():
    
    create_tab = createTab()
    edit_tab = editTab()
    delete_tab = deleteTab()

    layout = [[sg.TabGroup([[sg.Tab('Create User', create_tab), sg.Tab('Edit User', edit_tab), sg.Tab('Delete User', delete_tab)]])]]
    return layout


#function: main function. the app starts here
if __name__ == "__main__":    
    layout = createLayout()
    window = sg.Window('File Reader', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        print('You entered ', values)

    window.close()
    
