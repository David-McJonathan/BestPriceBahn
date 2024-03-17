from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions

import time
from datetime import datetime

import sqlDB

def start():


    print("Welcome to the search for the best train price")

    depature = str(input('Enter a different departure station (or skip): ') or "Hamburg Hbf")
    destinations = ["München Hbf", "Berlin Hbf", "Mainz Hbf", "Frankfurt Hbf"]


    connection = sqlDB.startSQLdb()

    options = ChromeOptions()
#    options.add_argument("--headless=new")
#    options.add_argument("--window-size=1920,1080")
#    driver.get_screenshot_as_file("screenshot.png")
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.bahn.de/")
    driver.implicitly_wait(1.5)
       
    
    preparationSearch(driver)

       
    driver.implicitly_wait(5)

    tripDate = datetime.now()


    for destination in destinations:

        changeOpen(driver)

        setDeparture(driver, depature)        
        setDestination(driver, destination)       
        time.sleep(1)
        
        changeDone(driver)
        
        time.sleep(3)

        activeBestpreis(driver)
        prices = getBestpreis(driver)
        sendSQL(connection, depature, destination, tripDate, prices)


    
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
    """
    Change Date
    :param driver: driver
    :param month: month in int
    :param day: day in int
    """

    monthNow = datetime.now().date().month

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
    """
    Set Departure
    :param driver: driver
    :param city: city in String
    """


    departure_Box = driver.find_element(by=By.CLASS_NAME, value="db-web-autocomplete.quick-finder-basic__stations-von-halt.test-von-halt").find_element(By.CSS_SELECTOR, "input")
    

    departure_Box.send_keys(Keys.CONTROL + "a")
    departure_Box.send_keys(Keys.DELETE)
    departure_Box.send_keys(city)

    driver.find_element(by=By.CLASS_NAME, value="quick-finder__content-wrapper").click()



def setDestination(driver, city):
    """
    Set Destination
    :param driver: driver
    :param city: city in String
    """


    destination_Box = driver.find_element(by=By.CLASS_NAME, value="db-web-autocomplete.quick-finder-basic__stations-nach-halt.test-nach-halt").find_element(By.CSS_SELECTOR, "input")
      

    destination_Box.send_keys(Keys.CONTROL + "a")
    destination_Box.send_keys(Keys.DELETE)
    destination_Box.send_keys(city)


    #driver.find_element(by=By.CLASS_NAME, value="quick-finder__content-wrapper").click()




def activeBestpreis(driver):


    if not driver.find_element(by=By.CLASS_NAME, value="db-web-switch-list__input").is_selected():

        try:
            driver.find_element(by=By.CLASS_NAME, value="db-web-switch-list--compact.db-web-switch-list.tagesbestpreis-toggle__switch").click()       
            time.sleep(1)

        except:
            print("---Not posible to active Bestpreis Switch---")
            
        


def getBestpreis(driver):

    driver.implicitly_wait(3)

    prices = driver.find_elements(By.CLASS_NAME, "tagesbestpreis-intervall__button-text")

    pricesFloat = []

    for e in prices:
        pricesFloat.append(convertElementToFloat(e))


    return pricesFloat




def sendSQL(connection, depature, destination, tripDate, prices):
    """
    Send data to DB
    :param connection: connection to the db
    :param depature: as String
    :param destination: as String
    :param tripDate: as String
    :param checkDate: as String
    :param preis: as Float array
    """

    if len(prices) == 6:

        checkDate = datetime.now()

        data = (depature, destination, tripDate, checkDate, prices[0], prices[1], prices[2], prices[3], prices[4], prices[5])

        with connection:            
            sqlDB.sendSQLdata(connection, data)





def convertElementToFloat(str):

    strNumber = str.text[3:-2]
    strNumber = strNumber.replace(',', '.')
    floNumber = float(strNumber)

    return floNumber

   




if __name__ == "__main__":
    start()












