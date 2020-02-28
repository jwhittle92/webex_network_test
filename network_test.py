from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import Tk
import time

driver = webdriver.Firefox()
web = driver.get("https://mediatest.ciscospark.com")
elem = driver.find_element_by_id('start_tests')
elem.click()

time.sleep(45)

app = driver.find_element_by_class_name('card-result-text.card-result-text-app-ok').text
room = driver.find_element_by_class_name('card-result-text.card-result-text-room-ok').text
call = driver.find_element_by_class_name('card-result-text.card-result-text-call-ok').text

lis = [app, room, call]
print(lis)

if app == 'Successful' and room == 'Successful' and call == 'Successful':
    print('The tests were successful')
else:
    # use the 'copy clipboard' function and save output to file
    copypaste = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/article/div[5]/div/a[2]')
    copypaste.click()
    #store clipboard in variable
    output = Tk().clipboard_get()
    print(str(output))
    #write variable to file
    log = open('webexlogs.txt', 'w+')
    log.write(output)
    log.close()

#driver.quit()
 



