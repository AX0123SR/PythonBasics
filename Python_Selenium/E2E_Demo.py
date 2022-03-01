from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:/Users/ayussriv/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
# //div[@class='card h-100']/div/h4/a
for product in products:
    product_name = product.find_element_by_xpath("div/h4/a").text
    if product_name == "Blackberry":
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector("a[class = 'nav-link btn btn-primary']").click()
driver.find_element_by_xpath("//button[@class = 'btn btn-success']").click()
driver.find_element_by_id("country").send_keys("Ind")
wait = WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element_by_link_text("India").click()

driver.find_element_by_xpath("//div[@class = 'checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("[type='submit']").click()
print(driver.find_element_by_class_name("alert-success").text)