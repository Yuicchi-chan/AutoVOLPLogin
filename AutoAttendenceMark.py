from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import sys
import time

chromeDriverPath = os.getcwd()+('\\chromedriver.exe')
username = sys.argv[1]
password = sys.argv[2]

chrome_Options = Options()
#chrome_Options.add_argument("--disable-gpu")
#chrome_Options.add_argument("--headless")
chrome_Options.add_argument("--disable-popup-blocking")
browser = webdriver.Chrome(chromeDriverPath, options=chrome_Options)
browser.get("https://wisdom.volp.in/")
#time.sleep(2)

input_Field_Username = browser.find_element_by_id('input-8')
input_Field_Username.send_keys(username)

input_Field_Passowrd = browser.find_element_by_id('input-12')
input_Field_Passowrd.send_keys(password)

button = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/center[4]/div/button/span')
button.click()
Script = 'var i = document.getElementsByClassName("v-card__title pointer");for (var x=0; x<i.length;x++){i[x].click();}'
Script2 = 'for (var x=0; x<i.length;x++){i[x].click();}'
time.sleep(2)
browser.execute_script('var i = document.getElementsByClassName("v-card__title pointer");for (var x=0; x<i.length;x++){i[x].click();}')
print("LOL")
time.sleep(2)
windows = browser.window_handles
browser.switch_to.window(windows[1])
#browser.switch_to.alert.dismiss()
browser.close()
browser.switch_to.window(windows[0])
print('Done!')
browser.quit()
exit(0)