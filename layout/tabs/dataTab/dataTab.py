import PySimpleGUI as sg
from operations.readFromJSON import readData
from styles.defaultStyles import default_text_style
from operations.processDataForTable import processDataForTable

#function: Edit tab layout for editing users
def dataTab():
    text_style = default_text_style()

    data = readData()
    data_headings = []
    if len(data) > 0:
        data_headings = list(data[0].keys())
        data = processDataForTable(data)

    return [
        [
            sg.Table(
                values=data, 
                headings=data_headings,
                max_col_width=100,
                auto_size_columns=False,
                display_row_numbers=True,
                vertical_scroll_only=False,
                def_col_width=20,
                justification='left',
                enable_events=True,
                font=text_style['font'],
                size=text_style['size'],
                num_rows=6, 
                key='_INFOTABLE_'
            )
        ]
    ]
    
