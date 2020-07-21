# reference:
# https://www.youtube.com/watch?v=7I2s81TsCnc
# https://www.youtube.com/watch?v=cnPlKLEGR7E
# https://gspread.readthedocs.io/en/latest/user-guide.html#getting-all-values-from-a-row-or-a-column
# https://techwithtim.net/tutorials/google-sheets-python-api-tutorial/
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://googleapis.com/auth/drive']

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('MerchantInfoRetrieval-c82f975851da.json', scope)

gc = gspread.authorize(credentials)

#Test worksheet
#wks = gc.open('StoreCardAccountTest').sheet1

#Working worksheet
wks = gc.open('StoreCardAccountVerifyChecklist').sheet1



#print(wks.get_all_records()) #Prints whole spreadsheet


def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def checkValidMPMnumber(MPMnumber):
    if len(MPMnumber) > 12 or len(MPMnumber) < 12:
        return False
    firstThree = MPMnumber[:-9]
    if firstThree != 'MPM':
        return False
    lastNine = MPMnumber[3:]
    if isInt(lastNine) == False:
        return False
    return True

def getMPMnumbersfromSpreadsheet():
    validMPMnumbers = wks.col_values(2)
    for i in range(len(validMPMnumbers)):
        checkValidMPMnumber(validMPMnumbers[i])
        if validMPMnumbers != True:
            del validMPMnumbers[i]
        return validMPMnumbers

def findMPMrow(MPMnumber):
    return wks.find(MPMnumber).row

def insertEmail(MPMnumber, email):
    cell = 'L' + (str(findMPMrow(MPMnumber)))
    wks.update_acell(cell, email)

def insertFname(MPMnumber, Fname):
    cell = 'M' + (str(findMPMrow(MPMnumber)))
    wks.update_acell(cell, Fname)

def insertLname(MPMnumber, Lname):
    cell = 'N' + (str(findMPMrow(MPMnumber)))
    wks.update_acell(cell, Lname)

def insertNumTransactions(MPMnumber, NumTransactions):
    cell = 'O' + (str(findMPMrow(MPMnumber)))
    wks.update_acell(cell, NumTransactions)

if __name__ == "__main__":
    Fname = 'James'
    Lname = 'Burch'
    email = 'example@gmail.net'


    num = (getMPMnumbersfromSpreadsheet())
    print(findMPMrow("MPM111111111"))
    insertEmail('MPM111111111', email)
    insertLname('MPM111111111', Fname)
    insertFname('MPM111111111', Lname)