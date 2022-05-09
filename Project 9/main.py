# import recommended packages
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# add chrome driver and options
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
service = ChromeService(
    executable_path=r"C:\Users\haris\AppData\Local\Programs\Python\Python310\Lib\site-packages\seleniumbase\drivers"
                    r"/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Add url you want to access
driver.get("https://www.goodreads.com/choiceawards/best-books-2021")

# add best books category in a easy to handle dictionary
categories = {els.text: els.get_attribute("href") for els in
              driver.find_elements(By.CSS_SELECTOR, "div.category.clearFix a") if
              els.get_attribute("href") != 'https://www.goodreads.com/choiceawards/best-books-2021#'}
print(categories)

time.sleep(3)
driver.close()
