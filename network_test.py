import time
from datetime import datetime
from selenium import webdriver
from tkinter import Tk
from twisted.internet import task, reactor

# How often the test runs in seconds
interval = 300.0

# Opens the webpage in FireFox, finds the 'Start Test' button, and clicks it. This assumes the user has a wired connection.
def webex_test():
    # Open FireFox and browse to the WebEx Network Test site ('mediatest.ciscospark.com')
    driver = webdriver.Firefox()
    driver.get("https://mediatest.ciscospark.com")
    #Locate the 'Start Test' button and click it. This assumes the user is using the default '
    elem = driver.find_element_by_id('start_tests')
    elem.click()

    # Wait some time for the network tests to complete
    time.sleep(45)

    # Locate the results after the tests have completed 
    app = driver.find_element_by_class_name('card-result-text.card-result-text-app-ok').text
    room = driver.find_element_by_class_name('card-result-text.card-result-text-room-ok').text
    call = driver.find_element_by_class_name('card-result-text.card-result-text-call-ok').text

    # Evaluate the results of the network test
    if app == 'Successful' and room == 'Successful' and call == 'Successful':
        print('The tests were successful')
    else:
        print('The tests were not successful')
        date = datetime.now()
        # use the 'copy clipboard' function and save output to file
        copypaste = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/article/div[5]/div/a[2]')
        copypaste.click()
        #store clipboard in variable
        output = Tk().clipboard_get()
        #write variable to file
        log = open('webexlogs-' + str(date) +'txt', 'w+')
        log.write(output)
        log.close()

    driver.quit()
    return 'The test has completed'


#Run the tests using specified interval
schedule = task.LoopingCall(webex_test)
schedule.start(interval)
reactor.run()
