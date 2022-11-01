
import PySimpleGUI as sg
from validation.isNameValid import isNameValid
from validation.isSalaryValid import isSalaryValid
from validation.isBirthdayValid import isBirthdayValid

#function: validate inputs for users
def isValid(values):
    name = values["-NAME-"]
    age = values["-SALARY-"]
    birthday = values["-BIRTHDAY-"]

    nameErrorFlag, nameErrorMsg = isNameValid(name)
    salaryErrorFlag, salaryErrorMsg = isSalaryValid(age)
    birthErrorFlag, birthErrorMsg = isBirthdayValid(birthday)
    
    errorMsg = ""
    if nameErrorFlag or salaryErrorFlag or birthErrorFlag:
        errorMsg += nameErrorMsg + " " + salaryErrorMsg + " " + birthErrorMsg
        sg.popup(errorMsg)
        return False
    else:
        return True
