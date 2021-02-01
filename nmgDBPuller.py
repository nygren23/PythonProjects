import os, sys
import io
import smartsheet # pip install smartsheet-python-sdk to work
import requests
import openpyxl # pip install openpyxl to work
import smartsheet.sheets


# PATHS ARE ABSOLUTE!

####################################
# pulling sheets from Smartsheet API
####################################

# initialize smartsheet client
try:
    smartsheet_client = smartsheet.Smartsheet('df2s5o5s2max9nkfg2jcou502l')

    # download sheet to my Desktop by sheet id
    filePath = os.path.dirname(sys.executable)

    print("Attempting download...")

    smartsheet_client.Sheets.get_sheet_as_excel(
        8007720352671620,
        filePath
    )

    print("Downloaded sheet...")

except Exception as e:
    print(e)

# delete 'Comments' sheet tab

workbook = openpyxl.load_workbook(filePath + '/NMG Main College Database.xlsx')
workbook.remove(workbook['Comments'])
workbook.save(filePath + '/NMG Main College Database.xlsx')

print("Deleted Comments tab")

