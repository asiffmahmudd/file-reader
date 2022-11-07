import PySimpleGUI as sg

from layout.tabs.usersTab.usersTab import usersTab
from layout.tabs.dataTab.dataTab import dataTab
from styles.defaultStyles import default_text_style

def tabsGroup():
    
    create_tab = usersTab()
    data_tab = dataTab()
    
    text_style = default_text_style()

    return sg.TabGroup(
        [
            [
                sg.Tab('Users', create_tab, key="-USERS_TAB-"), 
                sg.Tab('Data', data_tab, key="-DATA_TAB-"), 
            ]
        ],
        font=text_style["font"],
        enable_events=True,
    )