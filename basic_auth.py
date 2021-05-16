from selenium import webdriver
import os

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

log = ["a","bbb","asdf","xyz","admin"];

a=0

for i in log:
    driver.get("http://"+i+":"+i+"@the-internet.herokuapp.com/basic_auth")
    if "h3" in driver.page_source:
        print("\n!!!#!!!Correct login: "+i+" & password: "+i+"\n#TOTAL TRY: "+str(a+1))
    else:
        print(str(a)+"#Incorrect login: "+i+" & password: "+i)
        a=a+1
os.system("pause")
driver.quit()