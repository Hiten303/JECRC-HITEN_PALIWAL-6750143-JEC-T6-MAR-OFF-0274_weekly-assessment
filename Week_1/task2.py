from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()

sleep(3)

driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.wikipedia.org/")

search_input = driver.find_element(By.ID, "searchInput")

english_link = driver.find_element(By.CSS_SELECTOR, "a#js-link-box-en")

logo_image = driver.find_element(By.CSS_SELECTOR, "div.central-textlogo img")

language_links = driver.find_elements(By.CSS_SELECTOR, "div.central-featured-lang")
print("Number of language links in central block:", len(language_links))

driver.back()
sleep(1)


driver.forward()
sleep(1)


driver.refresh()
sleep(1)

print("Final page title:", driver.title)

driver.quit()