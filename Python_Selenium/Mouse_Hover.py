from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:/Users/ayussriv/Downloads/chromedriver_win32/chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
menu=driver.find_element_by_id("mousehover")
action.move_to_element(menu).perform()
child = driver.find_element_by_link_text("Reload")
action.move_to_element(child).click().perform()