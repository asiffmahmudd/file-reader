
import PySimpleGUI as sg

def clearInputs(keys_to_clear):
    window = sg.Window('File Reader')
    window["-NAME-"]('')
    window["-SALARY-"]('')
    window["-BIRTHDAY-"]('')