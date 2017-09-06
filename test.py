from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import Helper
import csv

server = Server("/Users/kaniska/browsermob-proxy/bin/browsermob-proxy")
server.start()
proxy = server.create_proxy()

profile = webdriver.FirefoxProfile()
profile.set_proxy(proxy.selenium_proxy())
driver = webdriver.Firefox(firefox_profile=profile)

proxy.new_har(ref="Test", options={'captureHeaders': 'true', 'captureContent': 'true'})

driver.get("https://www.google.co.in")
element = driver.find_element_by_xpath('//*[@id="lst-ib"]')
element.send_keys('datalicious')
element.send_keys(Keys.ENTER)
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "resultStats")))
    driver.find_element_by_xpath(".//*[@id='rso']/div[1]/div/div[1]/div/div/h3/a").click()
    print("Task 1 Completed")
except TimeoutException:
    print("It is taking more time")

time.sleep(15)

server.stop()
answer = proxy.har

requiredParameters = Helper.DataHelper().getRequiredDataFrom(answer)

with open('dict.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in requiredParameters.items():
       writer.writerow([key, value])
print("Task 3 Completed")

driver.quit()