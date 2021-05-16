from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

add = driver.find_element_by_xpath('//button[text()="Add Element"]')
for x in range(100):
    try:
        add.click()
        print("#Anwendung: hinzugefügt "+str(x+1)+" elements")
    except:
        print("\n!#! Anwendung: Error add.click() an "+str(x+1)+"position\n")
#first_search.send_keys(Keys.RETURN)

flag = False
while flag == False:
    inp = input("\n#?Anwendung: Möchten Sie die Elemente jetzt entfernen? Y/N\n")
    if inp == "Y":
        flag == True
        for a in range(100):
            rmv = driver.find_element_by_xpath('//button[text()="Delete"]')
            try:
                rmv.click()
                print("#Anwendung: entfernen "+str(a+1)+" obiekten")
            except:
                print("\n!#! Bug_report in ("+str(a+1)+")\n")
        print("\n#Anwendung: End anwendung\n")
        os.system("pause")
        driver.quit()
    elif inp == "N":
        flag == True
        print("\n#Anwendung: End anwendung\n")
        os.system("pause")
        driver.quit()
    else:
        print("\n!#! Anwendung: Geben Sie den richtigen Wert an!\n")