
import globalStore.globals as info
from operations.processDataForTable import processDataForTable
import globalStore.globals as globals

def updateTableData():
    tableData = processDataForTable(info.info)
    globals.window['-INFO_TABLE-'].update(tableData)