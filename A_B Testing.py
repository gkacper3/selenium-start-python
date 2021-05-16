from selenium import webdriver
import os

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://the-internet.herokuapp.com/abtest")

h = driver.find_element_by_tag_name('h3').text

p = driver.find_element_by_tag_name('p').text

print(h+"\n\n"+p)

print("Koniec aplikacji")
os.system("pause")
driver.quit()