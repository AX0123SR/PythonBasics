from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/ayussriv/Downloads/chromedriver_win32/chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_id("name").send_keys("Ayush")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert "Ayush" in alertText,"text is not there."
alert.accept()