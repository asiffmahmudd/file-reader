import PySimpleGUI as sg

#function: Create tab layout for adding users
def createTab():
    create_tab = [  
        [sg.Text("Name:", size=(6,0)), sg.Input("", pad=(10,10), key='-NAME-')], 
        [sg.Text("Salary:", size=(6,0)), sg.Input("", pad=(10,10), key='-SALARY-')], 
        [sg.Text("Birthday:", size=(6,0)), sg.Input("", disabled=True, pad=(10,10), key='-BIRTHDAY-'), sg.CalendarButton("Date Of Birth", close_when_date_chosen="True",  target="-BIRTHDAY-", no_titlebar=False, format='%Y-%m-%d')],
        [sg.Stretch(),sg.Button('Add', size=(8,1)), sg.Button('Cancel', pad=(10,5), size=(8,1))]
    ]
    return create_tab
