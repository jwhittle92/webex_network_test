from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import Tk

driver = webdriver.Firefox()
web = driver.get("https://mediatest.ciscospark.com")
elem = driver.find_element_by_id('start_tests')
elem.click()

test = WebDriverWait(driver, 30).until(EC.title_is("Test Results"))

app = driver.find_element_by_class_name('card-result-text card-result-text-app-ok').text
room = driver.find_element_by_class_name('card-result-text card-result-room-app-ok').text
call = driver.find_element_by_class_name('card-result-text card-result-call-app-ok').text


if app == 'Successful' and room == 'Successful' and call == 'Successful':
    print('The tests were successful')
else:
    # use the 'copy clipboard' function and save output to file
    
    #store clipboard in variable
    output = Tk().clipboard_get

    #write variable to file
    log = open('webexlogs.txt', 'w+')
    log.write(output)
    log.close()
 



