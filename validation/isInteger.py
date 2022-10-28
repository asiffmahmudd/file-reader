#funciton: checking if the value is an integer
def isInteger(value):
    try:
        #trying to convert the value into an int and return the value
        value = int(value) 
        return value
    except:
        #if the conversion fails, return false
        return False