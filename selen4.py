from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

ser = Service(PATH)
op = webdriver.ChromeOptions()
s = webdriver.Chrome(service=ser, options=op)
driver = s

#driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
#driver = webdriver.Chrome().install())

#driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(10)

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1,-1,-1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5):
    actions.perform()
    count = cookie_count.text
    print(count)