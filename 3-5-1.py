from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
ChromeDriver = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
driver = webdriver.Chrome(executable_path=ChromeDriver)
driver.get("http://www.python.org")
assert "Python" in driver.titl
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
time.sleep(10)
driver.close()
e
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")