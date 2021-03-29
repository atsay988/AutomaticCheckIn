
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

driver= webdriver.Chrome()
driver.get("http:/www.southwest.com/air/check-in/index.html")
assert "Southwest" in driver.title
driver.implicitly_wait(10)
#elem = driver.find_element_by_xpath("//button[@class='transition-background transition-actionable actionable-tab actionable-tab_huge tab-navigation--tab tab-navigation--tab_checkin']")
#driver.implicitly_wait(10)
#elem.click()
#driver.implicitly_wait(10)
#code = driver.find_element_by_xpath("//input[@id='LandingAirReservationSearchForm_confirmationNumber_check-in']").send_keys("ABCDEF")


cn = driver.find_element_by_id('confirmationNumber')
cn.send_keys("ABCDEF")
driver.implicitly_wait(4)

fn = driver.find_element_by_id('passengerFirstName')
fn.send_keys("Allison")

ln = driver.find_element_by_id('passengerLastName')
ln.send_keys("Tsay")

check_in = str(datetime(2021, 2, 27, 13, 33, 5).minute)

while True:
	now = str(datetime.now().minute)
	print(now)
	
	if now == check_in:
		print("true")
		break

submit = driver.find_element_by_id('form-mixin--submit-button')
submit.click()
