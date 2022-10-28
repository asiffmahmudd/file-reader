#function: checking if name is valid or not
def isNameValid(name):
    errorFlag = 0
    errorMsg = ""
    if name == "":
        errorFlag = 1
        errorMsg = "Name cannot be null. "
    if name and not name.isalpha():
        errorFlag = 1
        errorMsg += "Name should only contain alphabets"
    return [errorFlag, errorMsg]