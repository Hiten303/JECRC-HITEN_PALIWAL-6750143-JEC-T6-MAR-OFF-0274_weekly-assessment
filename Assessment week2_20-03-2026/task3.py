from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.google.com")

wait = WebDriverWait(driver, 10)

search_box = wait.until(EC.presence_of_element_located((By.XPATH,'//textarea[@class="gLFyf"]')))
search_box.send_keys("Selenium Python")


suggestions = wait.until( EC.presence_of_all_elements_located((By.XPATH, "//ul[@role='listbox']//li")))


print("Suggestions:")
for s in suggestions:
    print(s.text)

suggestions[1].click()


sleep(5)

driver.quit()