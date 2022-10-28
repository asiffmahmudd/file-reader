#function: checking if birthday is valid or not
from datetime import datetime
from time import time


def isBirthdayValid(birthday):
    errorFlag = 0
    errorMsg = ""
    if birthday == "":
        errorFlag = 1
        errorMsg = "Birthday cannot be null. "
    year, month, day = [int(d) for d in birthday.split("-")]
    if birthday and datetime(year,month,day) > datetime.now():
        errorFlag = 1
        errorMsg += "Birthday cannot be in future"
    return [errorFlag, errorMsg]