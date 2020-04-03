import time 
from sendalert import SendAlert
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from selenium import webdriver
from tkinter import Tk

# Opens the webpage in Chrome, finds the 'Start Test' button, and clicks it. This assumes the user has a wired connection.
def webex_test():
    # Open Chrome and browse to the WebEx Network Test site ('mediatest.ciscospark.com')
    driver = webdriver.Chrome(ChromeDriverManager().install())
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
        alert = SendAlert('The tests were successful')
        alert.send_alert()
    else:
        print('The tests were not successful')
        date = datetime.time(datetime.now())
        # use the 'copy clipboard' function and save output to file
        copypaste = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/article/div[5]/div/a[2]')
        copypaste.click()
        #store clipboard in variable
        output = Tk().clipboard_get()
        #write variable to file
        log = open('webexlogs-' + date.strftime('%m-%d-%H;%M;%S') + '.txt', 'w+')
        log.write(output)
        log.close()
        alert = SendAlert(output)
        alert.send_alert()
    driver.quit()
    return 'The test has completed'

if __name__ == "__main__":
    webex_test()

