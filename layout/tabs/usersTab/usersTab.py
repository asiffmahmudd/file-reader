import PySimpleGUI as sg
from operations.readFromJSON import readData
from styles.defaultStyles import default_text_style
from styles.defaultStyles import default_input_style

#function: Edit tab layout for editing users
def usersTab():
    text_style = default_text_style()
    input_style = default_input_style()

    data = readData()
    data_headings = []
    if len(data) > 0:
        data_headings = list(data[0].keys())
        data = processEditData(data)

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
        [
            sg.Table(
                values=data, 
                headings=data_headings,
                max_col_width=65,
                auto_size_columns=False,
                display_row_numbers=True,
                vertical_scroll_only=False,
                def_col_width=20,
                justification='left',
                enable_events=True,
                font=text_style['font'],
                size=text_style['size'],
                num_rows=6, 
                key='-INFO_TABLE-'
            )
        ]
    ]
    
def processEditData(data): 
    temp = []
    for row in data:
        rowData = []
        for val in row.values(): 
            rowData.append(val)
        temp.append(rowData)
    return temp