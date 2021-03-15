from selenium import webdriver
import  time

browser = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe')
browser.get('http://prerelease.simcards.cn/')
print(browser.title)
browser.maximize_window()
login_account_test = browser.find_element_by_xpath('//*[@id="pane-first"]/div/div[1]/div/input')
login_account_test.send_keys('sangjy')
login_password_test = browser.find_element_by_xpath('//*[@id="pane-first"]/div/div[2]/div/input')
login_password_test.send_keys('123456')
time.sleep(2)
browser.find_element_by_xpath('//*[@id="pane-first"]/div/div[3]/button/span').click()
time.sleep(2)

time.sleep(10)

browser.close()
