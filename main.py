from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions

import time
import datetime


def start():


    print("Welcome to the search for the best train price")
    
    depature = str(input('Enter a different departure station (or skip): ') or "Hamburg Hbf")
    destinations = ["München Hbf", "Berlin Hbf", "Mainz Hbf", "Frankfurt Hbf"]
    date = ""

    options = ChromeOptions()
#    options.add_argument("--headless=new")
#    options.add_argument("--window-size=1920,1080")
#    driver.get_screenshot_as_file("screenshot.png")
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.bahn.de/")
    driver.implicitly_wait(1.5)


    preparationSearch(driver)
    
    time.sleep(1)

    
    for destination in destinations:

        changeOpen(driver)

        setDeparture(driver, depature)        
        setDestination(driver, destination)       
        time.sleep(1)
        
        changeDone(driver)
        
        time.sleep(3)

        activeBestpreis(driver)
        prices = getBestpreis(driver)
        sendSQL(depature, destination, prices)




def preparationSearch(driver):

    removeCookieBanner(driver)
    openBahnStartseite(driver)
    time.sleep(1)
       
    changeOpen(driver)
    setDate(driver, 7, 5)
           
    changeDone(driver)

    



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
    
    driver.find_element(by=By.CLASS_NAME, value="reise-daten-zusammenfassung__button").click()


def changeDone(driver):

    driver.find_element(by=By.CLASS_NAME, value="db-web-button.test-db-web-button.db-web-button--type-primary.db-web-button--size-large.quick-finder-basic__search-btn.quick-finder-basic__search-btn--desktop").click()



def setDate(driver, month, day):


    monthNow = datetime.datetime.now().date().month

    driver.find_element(by=By.CLASS_NAME, value="open-overlay-button.button-overlay__button").click()

    time.sleep(0.25)

    month_Button = driver.find_element(by=By.CLASS_NAME, value="db-web-button.test-db-web-button.db-web-button--type-text.db-web-button--size-large.db-web-button--type-plain.db-web-date-picker-month-bar__right-handle")


    for i in range(month - monthNow):

        month_Button.click()
        time.sleep(0.01)

    
    active_Slider = driver.find_element(by=By.CLASS_NAME, value="swiper-slide.swiper-slide-active")
    days_Button = active_Slider.find_elements(by=By.CLASS_NAME, value="db-web-date-picker-calendar-day.db-web-date-picker-calendar-day--day-in-month-or-selectable")

    days_Button[day-1].click()
    time.sleep(0.25)

    driver.find_element(by=By.CLASS_NAME, value="quick-finder-overlay-control-buttons.quick-finder-zeitauswahl-content__control-buttons").click()





def setDeparture(driver, city):

    print("ToDo: setDeparture")



def setDestination(driver, city):

   print("ToDo: setDestination")



def activeBestpreis(driver):


    if not driver.find_element(by=By.CLASS_NAME, value="db-web-switch-list__input").is_selected():

        try:
            driver.find_element(by=By.CLASS_NAME, value="db-web-switch-list--compact.db-web-switch-list.tagesbestpreis-toggle__switch").click()       
            time.sleep(1)

        except:
            print("---Not posible to active Bestpreis Switch---")


def getBestpreis(driver):

    driver.implicitly_wait(3)

    prices = driver.find_elements(By.CLASS_NAME, "reise-preis__preis")

    return prices



def sendSQL(depature, destination, prices):

    if len(prices) > 0:

        print("(dummy) Sending to SQL-Database...")        
        print("(" + depature +") --> (" + destination + ")")

        for e in prices:
            print(convertElementToFloat(e))

        print("... Finish sending to SQL-Database")


def convertElementToFloat(str):

    strNumber = str.text[3:-2]
    strNumber = strNumber.replace(',', '.')
    floNumber = float(strNumber)

    return floNumber

   




if __name__ == "__main__":
    start()












