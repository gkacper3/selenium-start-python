from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://the-internet.herokuapp.com/checkboxes")

oi = driver.find_elements_by_xpath('//input')

a=0

for x in oi:
    print("#System: checkbox["+str(a)+"] is "+str(oi[a].is_selected()))
    a=a+1

print("\n#Anwendung: End anwendung\n")
os.system("pause")
driver.quit()