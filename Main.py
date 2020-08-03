from SupportDatabaseAccess import *
from GoogleSheetAccess import *
import time


def Main():
    driver = loginSupportDB()
    MPMnumbers = getMPMnumbersfromSpreadsheet()
    #print(MPMnumbers)
    for i in range(len(MPMnumbers)):
        switchMPMaccount(driver , MPMnumbers[i])
        # unquote below to fill in contact info too
        '''
        FirstName = getFname(driver)
        LastName = getLname(driver)
        Email = getEmail(driver)
        insertEmail(MPMnumbers[i], Email)
        insertLname(MPMnumbers[i], LastName)
        insertFname(MPMnumbers[i], FirstName)

        time.sleep(1)
        '''

        '''
        print("MPM: " , MPMnumbers[i])
        print("First Names: " , FirstName)
        print("Last Names: ", LastName)
        print("Email: ", Email)
        print("\n\n\n")
        '''
        try:
            numerberOfTransactions = numberOfStoreCardTransactions(driver, MPMnumbers[i])
        except NoSuchElementException:
            numerberOfTransactions = 'NA'
        if type(numerberOfTransactions) == type(int):
            if numerberOfTransactions > 99:
                numerberOfTransactions = '+99'
        #print("Number: ", numerberOfTransactions , type(numerberOfTransactions))
        #print(numerberOfTransactions)
        insertNumTransactions(MPMnumbers[i], numerberOfTransactions)
        #insertEmail(MPMnumbers[i], Email)
        #insertLname(MPMnumbers[i], LastName)
        #insertFname(MPMnumbers[i], FirstName)
        #time.sleep(1)
Main()
