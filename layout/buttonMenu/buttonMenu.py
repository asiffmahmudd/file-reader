import PySimpleGUI as sg
from styles.defaultStyles import default_btn_style

def buttonM():
    
    btn_style = default_btn_style()

    return [
        [
            sg.Button(
                'Add', 
                size=(8,1),
                font=btn_style["font"],
                key='-ACTION_BTN-',
                enable_events=True
            ), 
            sg.Button(
                'Cancel', 
                pad=(10,5), 
                size=(8,1),
                font=btn_style["font"]
            )
        ]
    ]