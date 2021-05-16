from selenium import webdriver
import requests
import os

PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://the-internet.herokuapp.com/broken_images")

img_arr = driver.find_elements_by_tag_name("img")

a=0

for one_img in img_arr:
    response = requests.get(one_img.get_attribute('src'), stream=True)
    if(response.status_code != 200):
        print("\n!!!Not Found: "+one_img.get_attribute('outerHTML')+" !!!\n")
        a=a+1
if a==0:
    print("$Raport: Broken images not found!!!")
else:
    print("$Raport: Total find "+str(a))
os.system("pause")
driver.quit()