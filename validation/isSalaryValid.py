from validation.isInteger import isInteger
from validation.isPositive import isPositive

#function: checking if age is valid or not
def isSalaryValid(age):
    errorFlag = 0
    errorMsg = ""
    if not isInteger(age):
        errorFlag = 1
        errorMsg = "Salary should contain an integer value. "
    if not errorFlag and not isPositive(age):
        errorFlag = 1
        errorMsg += "Salary should be a positive value"
    return [errorFlag, errorMsg]