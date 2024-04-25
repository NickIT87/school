from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to a website
driver.get("https://www.google.com")

# You can perform various actions here, such as scraping data or interacting with elements
time.sleep(20)

# Once done, close the browser
driver.quit()