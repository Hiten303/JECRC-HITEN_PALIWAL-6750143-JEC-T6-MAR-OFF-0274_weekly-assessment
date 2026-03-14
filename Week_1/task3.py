from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()

driver = webdriver.Chrome(options=chrome_options)


websites = [
    "https://www.souledstore.com/",
    "https://www.nike.com/",
    "https://www.bbc.com/news",
    "https://www.python.org/"
]


for url in websites:
    sleep(3)
    driver.get(url)

    print("Title ", driver.title)



driver.quit()