
import globalStore.globals as globals

#clears the inputs of the given keys
def clearInputs():#keysToClear):
    globals.window['-NAME-'].update('')
    globals.window['-SALARY-'].update('')
    globals.window['-BIRTHDAY-'].update('')
    # for key in keysToClear:
    #     globals.window[key].update('')