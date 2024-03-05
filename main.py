from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions


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

    getBestpreis(driver)
  


    



def removeCookieBanner(driver):

    time.sleep(2)

    shadow_host = driver.find_element(By.TAG_NAME, "div")
    shadow_root = shadow_host.shadow_root
    shadow_content = shadow_root.find_element(By.CLASS_NAME, 'btn.btn--secondary.js-accept-essential-cookies')

    shadow_content.click()




def openBahnStartseite (driver):

    print("ToDo: openBahnStartseite")
   

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

    print("ToDo: getBestpreis")



def convertElementToFloat(str):

    print("ToDo: convertElementToFloat")

   




if __name__ == "__main__":
    start()












