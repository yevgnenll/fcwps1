__author__="seungkwon"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver = webdriver.PhantomJS(executable_path='/usr/local/lib/node_modules/phantomjs/bin/phantomjs')
driver.get("https://www.facebook.com/groups/backtothemac/permalink/1615391905366375/")
driver.save_screenshot('orico.jpg')


# assert "Python" in driver.title
# elem = driver.find_elements_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No result found." not in driver.page_source
# print(driver.page_source)
# driver.close()