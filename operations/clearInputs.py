
import PySimpleGUI as sg

#clears the inputs of the given keys
def clearInputs(window, keysToClear):
    for key in keysToClear:
        window[key].update('')