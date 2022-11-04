
from layout.buttonMenu.buttonMenu import buttonM
from layout.statusBar.statusBar import statusBar
from layout.tabs.tabsGroup import tabsGroup

#function: adding all the tabs together and creating the window layout for the app
def createLayout():
    button_menu = buttonM()
    status_bar = statusBar()
    tab_group = tabsGroup()

    layout = [
        [button_menu],
        [tab_group],
        [status_bar]
    ]
    return layout