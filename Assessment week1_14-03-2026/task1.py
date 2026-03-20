from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()


driver = webdriver.Chrome(options=chrome_options)


driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")


password = driver.find_element(By.CSS_SELECTOR, "input#password")

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

footer_link = driver.find_element(By.CSS_SELECTOR, "div#page-footer a")


driver.quit()