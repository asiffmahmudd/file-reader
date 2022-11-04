import PySimpleGUI as sg
from styles.defaultStyles import default_text_style
from styles.defaultStyles import default_input_style

#function: Create tab layout for adding users
def createTab():

    text_style = default_text_style()
    input_style = default_input_style()

    return [  
        #row - 1
        [
            sg.Text(
                "Name:", 
                size=text_style["size"],
                font=text_style["font"]
            ), 
            sg.Input(
                "", 
                pad=input_style["pad"], 
                font=input_style["font"], 
                key='-NAME-'
            )
        ], 
        
        #row - 2
        [
            sg.Text(
                "Salary:", 
                size=text_style["size"],
                font=text_style["font"]
            ), 
            sg.Input(
                "", 
                pad=input_style["pad"],  
                font=input_style["font"],
                key='-SALARY-'
            )
        ], 
        
        #row - 3
        [
            sg.Text(
                "Birthday:", 
                size=text_style["size"],
                font=text_style["font"]
            ), 
            sg.Input(
                "", 
                disabled=True, 
                pad=input_style["pad"],  
                font=input_style["font"],
                key='-BIRTHDAY-'
            ), 
            sg.CalendarButton(
                "Date Of Birth", 
                close_when_date_chosen="True",  
                target="-BIRTHDAY-", 
                no_titlebar=False, 
                format='%Y-%m-%d',
                font=("Arial", 15)
            )
        ],
        
        #row - 4
        
    ]
