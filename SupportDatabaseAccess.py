from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import re


def loginSupportDB():
    path = "./geckodriver"
    driver = webdriver.Firefox(executable_path=path)
    driver.get("https://www.mycryptopay.com/devel/genesys/index.php")
    driver.find_element_by_name("username").send_keys("config.username")
    driver.find_element_by_name("password").send_keys("config.password")
    driver.find_element_by_name("submit_login").click()
    return driver

def switchMPMaccount(driver, MPMnumber):
    driver.get("https://www.mycryptopay.com/devel/genesys/index.php?page=editcustomer&siteid=" + MPMnumber)

def getFname(driver):
    return driver.find_element_by_name("first_name").get_attribute("value")

def getLname(driver):
    return driver.find_element_by_name("last_name").get_attribute("value")

def getEmail(driver):
    return driver.find_element_by_name("email").get_attribute("value")

def numberOfStoreCardTransactions(driver, MPMnumber):
    driver.get("https://www.mycryptopay.com/devel/genesys/index.php?page=customer&siteid=" + MPMnumber)
    driver.find_element_by_link_text("Log in as Customer").click()
    driver.get("https://www.mycryptopay.com/devel/login/index.php?page=viewstorecardtransactions")
    driver.find_element_by_id("siteselect_" + MPMnumber).click()
    html_source = driver.page_source
    Transactions = html_source.count("StoreCard") - 1
    return int(Transactions)



if __name__ == "__main__":
    driver =  loginSupportDB()
    #switchMPMaccount(driver, 'MPM012390529')
    '''
    print(getFname(driver))
    print(getLname(driver))
    print(getEmail(driver))
    '''
    print(numberOfStoreCardTransactions(driver, "MPM520452095"))
    #driver.get("https://www.mycryptopay.com/devel/genesys/index.php?page=customer&siteid=MPM674516021")
    #driver.find_element_by_link_text("Log in as Customer").click()
    #time.sleep(5)
    #driver.get("https://www.mycryptopay.com/devel/login/index.php?page=viewstorecardtransactions")
    #driver.find_element_by_id("siteselect_MPM695064218").click()
    #html_source = driver.page_source
    #print(html_source.count("StoreCard"))
    #print(html_source)
    #numberOfStoreCards = re.findall(re, "StoreCard")
    #driver.find_element_by_xpath('//href[@id="inner"]/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/a').click()
    #time.sleep(1)
