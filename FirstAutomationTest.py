from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://www.google.com")

driver.maximize_window()

print(driver.title)

driver.close()
