import os
import PySimpleGUI as sg
from csv import DictWriter

# from macpath import dirname
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

#function for writing data into a csv file
def writeToCSV(data):
    # open the file in the write mode
    filePath = ROOT_DIR + '\data\\' + "userdata.csv"
    mode = ''
    header = list(data.keys())

    if os.path.exists(filePath):
        mode = 'a'
    else:
        mode = 'w'

    with open(filePath, mode, newline='') as f_object:
 
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = DictWriter(f_object, fieldnames=header)
        if mode == 'w':
            writer_object.writeheader()
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(data)
        sg.popup("User added!")
        # Close the file object
        f_object.close()
    
