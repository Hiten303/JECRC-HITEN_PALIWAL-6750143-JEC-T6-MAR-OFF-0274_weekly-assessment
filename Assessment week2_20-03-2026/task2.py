from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://automationexercise.com")
driver.find_element(By.XPATH,'//a[text()=" Signup / Login"]').click()

wait = WebDriverWait(driver, 10)
name=driver.find_element(By.XPATH, '//input[@placeholder="Name"]').send_keys("Hiten Paliwal")
sleep(2)

email=driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]').send_keys("hiwal097@gmail.com")
sleep(2)
wait.until(EC.element_to_be_clickable(((By.XPATH, '//button[@data-qa="signup-button"]')))).click()
wait.until(EC.url_contains("signup"))
wait.until(EC.presence_of_element_located((By.XPATH,'//input[@value="Mr"]'))).click()
sleep(2)

newsletter=driver.find_element(By.ID,"newsletter")
newsletter.click()
offer=driver.find_element(By.ID,"optin")
offer.click()


sleep(2)

driver.quit()