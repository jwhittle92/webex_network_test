from selenium import webdriver

driver = webdriver.Firefox()
web = driver.get("https://mediatest.ciscospark.com")
elem = driver.find_element_by_id('start_tests')
elem.click()


app = driver.find_element_by_class_name('card-result-text card-result-text-app-ok').text
room = driver.find_element_by_class_name('card-result-text card-result-room-app-ok').text
call = driver.find_element_by_class_name('card-result-text card-result-call-app-ok').text







