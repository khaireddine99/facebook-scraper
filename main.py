from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.webdriver.common.keys import Keys



# option to keep the chrome driver open and click the not now thingy :)
chr_options = Options()
chr_options.add_experimental_option("detach", True)
prefs = {"profile.default_content_setting_values.notifications" : 2}
chr_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=chr_options)
driver.get("https://www.facebook.com/")
print(driver.title)

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

#enter username and password
username.clear()
username.send_keys("xx@gmail.com")
password.clear()
password.send_keys("xx")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

#We are logged in!

time.sleep(3)

# get to the post
driver.get("https://www.facebook.com/photo/?fbid=315635924372096&set=gm.2118155795021720&idorvanity=1519983794838926")
time.sleep(2)


# leave a comment under the post
comment_area = driver.find_element(By.XPATH, "//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r']")
comment_area.send_keys("comment made by a bot")
comment_area.send_keys(Keys.ENTER)










                                               










