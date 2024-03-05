from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions

import time
import datetime


def start():


    print("Welcome to the search for the best train price")


    depature = "Hamburg Hbf"
    destination = "Frankfurt Hbf"
    date = ""

    options = ChromeOptions()
#    options.add_argument("--headless=new")
#    options.add_argument("--window-size=1920,1080")
#    driver.get_screenshot_as_file("screenshot.png")
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.bahn.de/")
    driver.implicitly_wait(1.5)
       
    
    removeCookieBanner(driver)
    openBahnStartseite(driver)


    changeOpen(driver)

    setDate(driver, date)
    setDeparture(driver, depature)        
    setDestination(driver, destination)

    changeDone(driver)


    prices = getBestpreis(driver)
       

    for e in prices:
        print(convertElementToFloat(e))



    



def removeCookieBanner(driver):

    time.sleep(2)

    shadow_host = driver.find_element(By.TAG_NAME, "div")
    shadow_root = shadow_host.shadow_root
    shadow_content = shadow_root.find_element(By.CLASS_NAME, 'btn.btn--secondary.js-accept-essential-cookies')

    shadow_content.click()




def openBahnStartseite (driver):

    
  
    time.sleep(2)

    departure_Box = driver.find_element(by=By.CLASS_NAME, value="db-web-autocomplete.quick-finder-basic__stations-von-halt.test-von-halt").find_element(By.CSS_SELECTOR, "input")
    destination_Box = driver.find_element(by=By.CLASS_NAME, value="db-web-autocomplete.quick-finder-basic__stations-nach-halt.test-nach-halt").find_element(By.CSS_SELECTOR, "input")
    button_Search = driver.find_element(by=By.CLASS_NAME, value="db-web-button.test-db-web-button.db-web-button--type-primary.db-web-button--size-large.quick-finder-basic__search-btn.quick-finder-basic__search-btn--desktop")#.find_element(By.CSS_SELECTOR, "button")


    departure_Box.send_keys("Hamburg Hbf")
    destination_Box.send_keys("Köln hbf")
    driver.find_element(by=By.CLASS_NAME, value="db-web-autocomplete.quick-finder-basic__stations-von-halt.test-von-halt").click()

    time.sleep(1)

    button_Search.click()
    
    time.sleep(3)
   
    

def changeOpen(driver):
    
    print("ToDo: changeOpen")


def changeDone(driver):

    print("ToDo: changeDone")    



def setDate(driver, date):

    print("ToDo: setDate")


def setDeparture(driver, city):

    print("ToDo: setDeparture")



def setDestination(driver, city):

   print("ToDo: setDestination")






def getBestpreis(driver):

    driver.implicitly_wait(3)

    prices = driver.find_elements(By.CLASS_NAME, "reise-preis__preis")

    return prices




def convertElementToFloat(str):

    strNumber = str.text[3:-2]
    strNumber = strNumber.replace(',', '.')
    floNumber = float(strNumber)

    return floNumber

   




if __name__ == "__main__":
    start()












