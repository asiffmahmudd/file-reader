import PySimpleGUI as sg
from layout.tabs.createTab import createTab
from layout.tabs.deleteTab import deleteTab
from layout.tabs.editTab import editTab

#function: adding all the tabs together and creating the window layout for the app
def createLayout():
    create_tab = createTab()
    edit_tab = editTab()
    delete_tab = deleteTab()

    layout = [[sg.TabGroup([[sg.Tab('Create User', create_tab), sg.Tab('Edit User', edit_tab), sg.Tab('Delete User', delete_tab)]])]]
    return layout