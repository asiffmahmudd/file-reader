import PySimpleGUI as sg
import datetime

def statusBar():
    
    styles = {
        "font": ("Arial", 16),
        "background_color": "black"
    }

    curr_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return [
        [
            sg.Text(
                "Version: 1.0.1",
                font=styles["font"],
                key='-VERSION-'
            ),
            sg.Stretch(),
            sg.Text(
                curr_date,
                font=styles["font"],
                key='-DATE-'
            )
        ]
    ]