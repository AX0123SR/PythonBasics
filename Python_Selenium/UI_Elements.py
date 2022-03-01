from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/ayussriv/Downloads/chromedriver_win32/chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute('name') == "checkBoxOption2":
        checkbox.click()
        assert checkbox.is_selected(),"Checkboxes are not selected"

