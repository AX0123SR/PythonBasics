from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

s= Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=s)
driver.get("https://login.salesforce.com/?locale=eu")


#print(driver.find_element_by_xpath("//form[@name='login']/label").text)

print(driver.find_element(By.XPATH,"//form[@name='login']/div[1]/label").text)
print(driver.find_element(By.XPATH,"//form[@name='login']/label").text)

