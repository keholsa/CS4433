from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.headless = True
options.add_argument("--window-size=800,600")

driver = webdriver.Chrome('C:/Users/Keenan/Desktop/Python Files/chromedriver')

driver.get('https://universitycollege.okstate.edu/lasso/')
# driver.get('https://slate.okstate.edu/portal/lasso_tutoring')

submitFirst = driver.find_element_by_xpath('//*[@id="main-content"]/div[1]/div/aside/div/div[2]/span[2]/a').click()

username = driver.find_element_by_id('username').send_keys('keenan.holsapple@okstate.edu')
password = driver.find_element_by_id('password').send_keys('gLOOB198106')

submitLogin = driver.find_element_by_name('submit').click()

time.sleep(3)

sendPass = driver.find_element_by_xpath('//*[@id="auth-view-wrapper"]/div[2]/div[3]/button').click()

time.sleep(15)

trust = driver.find_element_by_id('trust-browser-button').click()

time.sleep(10)

XPATHTITLE= '//*[@id="portal_datepicker_'
XPATHTALBE1 = ']/div/table/tbody/tr['
XPATHTABLE2 = ']/td['
XPATHTABLE3 = ']'
xPathAddress = ""
xPathDate = ""

fullAddresses = driver.find_elements_by_xpath('//*[@id="portal_datepicker_f8a7e0fc-31b5-4886-87e6-8846766119d5"]')
for fullAddress in fullAddresses:
    fullAddress.get_attribute(id)

for x in range (1,8)
    for y in range(1,5)
x = 3
y = 3

test_date_click = driver.find_element_by_xpath(XPATHTITLE + 'f8a7e0fc-31b5-4886-87e6-8846766119d5\"' + XPATHTABLE1 + str(x) + XPATHTABLE2 + str(y) + XPATHTABLE3).click()
