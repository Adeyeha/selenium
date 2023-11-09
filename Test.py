from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import re
import random
import pandas as pd

class DemoFindElementByIDandName():
    def locate_by_id(self,description,country,name):
        driver = webdriver.Chrome()
        driver.get("https://nupsych.qualtrics.com/jfe/form/SV_8G16WmnqsgPkaq2")
        driver.maximize_window()
        # driver.find_element("id", "lst-ib").send_keys("Selenium")
        time.sleep(4)
        driver.find_element("id", "NextButton").click()
        time.sleep(4)
        driver.find_element("id", "QID5-1-label").click()
        time.sleep(4)
        driver.find_element("id", "NextButton").click()
        time.sleep(4)
        driver.find_element("id", "submit_intro").click()
        time.sleep(4)
        driver.find_element("id", "username").send_keys(name.strip())
        time.sleep(4)
        driver.find_element("id", "submit_username").click()
        time.sleep(4)
        driver.find_element("id", f"avatar{str(random.randint(1, 100))}").click() # 26 is the number of the avatar up to 100
        time.sleep(4)
        driver.find_element("id", "submit_avatar").click()
        time.sleep(4)
        # driver.find_element("id", "description").send_keys("""I'm a computer guru by day and a fun lover at night.\nI love to party and visit the most exquisite places around the world. \nA fun fact about me is that I've lived in 4 continents in the world and have visited every continent at least twice. \nYou can catch in basking in the sun or enjoying mimosa under the sunset.""")
        driver.find_element("id", "description").send_keys(description.strip())
        time.sleep(4)
        driver.find_element("id", "submit_text").click()
        time.sleep(4)
        driver.find_element("id", "submit_fb_intro").click()
        time.sleep(10)
        driver.find_element("id", "submit_fb_login").click()
        likes = driver.find_elements(By.CLASS_NAME, "btn-like")
        for x in range(0,len(likes)):
            if likes[x].is_displayed():
                likes[x].click()
        time.sleep(200)
        # className btn pull-right btn-like btn-custom btn-deround
        # className badge badge-custom  #Get Text
        NoOfLikes = int(driver.find_element(By.CLASS_NAME, "userslikes").text.strip())
        print(f"Number of likes:  {NoOfLikes}")
        driver.find_element("id", "final-continue").click()
        time.sleep(4)
        driver.find_element("id", "NextButton").click()
        time.sleep(4)
        driver.find_element("id", "QID19-1-label").click()
        driver.find_element("id", "QID20-1-label").click()

        QueLikes = driver.find_element(By.CSS_SELECTOR, "div[id='QID34'] strong").text
        QueLikes = int(re.findall(r'\d+', QueLikes)[0])

        if NoOfLikes < QueLikes:
            driver.find_element("id", "QID34-1-label").click()
        elif NoOfLikes == QueLikes:
            driver.find_element("id", "QID34-2-label").click()
        else:
            driver.find_element("id", "QID34-3-label").click()
        
        if NoOfLikes == 1:
            driver.find_element("id", "QID17-1-label").click()
        elif NoOfLikes == 10:
            driver.find_element("id", "QID17-2-label").click()
        elif NoOfLikes == 45:
            driver.find_element("id", "QID17-3-label").click()
        else :
            driver.find_element("id", "QID17-4-label").click()
        
        time.sleep(4)
        driver.find_element("id", "NextButton").click()
        time.sleep(4)
        driver.find_element("id", "NextButton").click()

        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, f"label[for='QR~QID29~1~{str(random.randint(1, 5))}']").click()
        driver.find_element(By.CSS_SELECTOR, f"label[for='QR~QID30~4~{str(random.randint(1, 5))}']").click()
        driver.find_element(By.CSS_SELECTOR, f"label[for='QR~QID30~5~{str(random.randint(1, 5))}']").click()
        driver.find_element(By.CSS_SELECTOR, f"label[for='QR~QID31~1~{str(random.randint(1, 5))}']").click()
        driver.find_element(By.CSS_SELECTOR, f"label[for='QR~QID31~2~{str(random.randint(1, 5))}']").click()
        driver.find_element(By.CSS_SELECTOR, f"label[for='QR~QID31~3~{str(random.randint(1, 5))}']").click()
        driver.find_element(By.CSS_SELECTOR, f"label[for='QR~QID31~4~{str(random.randint(1, 5))}']").click()
        driver.find_element(By.CSS_SELECTOR, f"label[for='QR~QID31~5~{str(random.randint(1, 5))}']").click()
        time.sleep(4)
        driver.find_element("id", "NextButton").click()
        time.sleep(4)
        driver.find_element(By.XPATH, f"(//label[contains(@for,'QR~QID2~1~{str(random.randint(1, 7))}')])[1]").click()
        driver.find_element(By.XPATH, f"(//label[contains(@for,'QR~QID2~2~{str(random.randint(1, 7))}')])[1]").click()
        driver.find_element(By.XPATH, f"(//label[contains(@for,'QR~QID2~3~{str(random.randint(1, 7))}')])[1]").click()
        driver.find_element(By.XPATH, f"(//label[contains(@for,'QR~QID2~4~{str(random.randint(1, 7))}')])[1]").click()
        driver.find_element(By.XPATH, f"(//label[contains(@for,'QR~QID2~5~{str(random.randint(1, 7))}')])[1]").click()
        driver.find_element(By.XPATH, f"(//label[contains(@for,'QR~QID2~6~{str(random.randint(1, 7))}')])[1]").click()
        driver.find_element(By.XPATH, f"(//label[contains(@for,'QR~QID2~7~{str(random.randint(1, 7))}')])[1]").click()
        driver.find_element(By.XPATH, f"(//label[contains(@for,'QR~QID2~8~{str(random.randint(1, 7))}')])[1]").click()
        time.sleep(4)
        driver.find_element("id", "NextButton").click()
        time.sleep(4)
        driver.find_element("id", f"QID60-{str(random.randint(1, 2))}-label").click()
        driver.find_element("id", f"QID61-{str(random.randint(1, 2))}-label").click()
        driver.find_element("id", f"QID62-{str(random.randint(1, 2))}-label").click()
        driver.find_element("id", f"QID63-{str(random.randint(1, 2))}-label").click()
        driver.find_element("id", f"QID64-{str(random.randint(1, 2))}-label").click()
        driver.find_element("id", f"QID65-{str(random.randint(1, 2))}-label").click()
        driver.find_element("id", f"QID66-{str(random.randint(1, 2))}-label").click()
        driver.find_element("id", f"QID67-{str(random.randint(1, 2))}-label").click()
        driver.find_element("id", f"QID68-{str(random.randint(1, 2))}-label").click()
        driver.find_element("id", f"QID69-{str(random.randint(1, 2))}-label").click()
        driver.find_element("id", f"QID70-{str(random.randint(1, 2))}-label").click()
        driver.find_element("id", f"QID71-{str(random.randint(1, 2))}-label").click()
        driver.find_element("id", f"QID72-{str(random.randint(1, 2))}-label").click()
        driver.find_element("id", f"QID73-{str(random.randint(1, 2))}-label").click()
        driver.find_element("id", f"QID74-{str(random.randint(1, 2))}-label").click()
        driver.find_element("id", f"QID75-{str(random.randint(1, 2))}-label").click()
        time.sleep(4)
        driver.find_element("id", "NextButton").click()
        time.sleep(4)
        driver.find_element("id", "QID52-4-label").click()
        driver.find_element("id", "QID53-2-label").click()
        time.sleep(4)
        driver.find_element("id", "NextButton").click()
        time.sleep(4)
        driver.find_element("id", "QR~QID11").send_keys(str(random.randint(18, 36)))
        driver.find_element("id", "QID12-3-label").click()
        Select(driver.find_element("id", "QR~QID13")).select_by_index(random.randint(1, 17))
        driver.find_element("id", "QR~QID14").send_keys(country.strip())
        time.sleep(3)
        driver.find_element("id", "NextButton").click()
        time.sleep(3)
        driver.find_element("id", "NextButton").click()
        time.sleep(10)
        driver.quit()

dt =pd.read_csv("fowosere.csv")
# dt=pd.read_excel("fowosere.xlsx")
dt.dropna(inplace=True)
# print(dt.to_dict('records'))

for x in dt.to_dict('records'):
    findbyid = DemoFindElementByIDandName()
    findbyid.locate_by_id(description = x['description'],country = x['country'],name= x['name'])
    print(f"Processed {x['name']} from {x['country']}")
# findbyid = DemoFindElementByIDandName()
# findbyid.locate_by_id()

