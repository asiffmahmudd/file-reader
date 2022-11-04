import PySimpleGUI as sg

from layout.tabs.createTab.createTab import createTab
from layout.tabs.deleteTab.deleteTab import deleteTab
from layout.tabs.editTab.editTab import editTab
from styles.defaultStyles import default_text_style

def tabsGroup():
    
    create_tab = createTab()
    edit_tab = editTab()
    delete_tab = deleteTab()
    
    text_style = default_text_style()

    return sg.TabGroup(
        [
            [
                sg.Tab('Create User', create_tab, key="-CREATE_TAB-"), 
                sg.Tab('Edit User', edit_tab, key="-EDIT_TAB-"), 
                sg.Tab('Delete User', delete_tab, key="-DELETE_TAB-")
            ]
        ],
        font=text_style["font"],
        enable_events=True
    )