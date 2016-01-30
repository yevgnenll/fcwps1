#input id="id"
#password id="pwd"

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.PhantomJS(executable_path='/usr/local/lib/node_modules/phantomjs/bin/phantomjs')
# driver.get("http://www.naver.com")
# driver.find_elements_by_id("id").send_keys('vanuel')
# driver.find_elements_by_id("pw").send_keys('qkdlfjf012!')
#
# driver.save_screenshot("status.jpg")
#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS('/usr/local/lib/node_modules/phantomjs/bin/phantomjs')
driver.get('http://www.naver.com')
driver.find_element_by_id('id').send_keys('spark0017')
driver.find_element_by_id('pw').send_keys('seung0018!')
driver.find_element_by_id('pw').send_keys(Keys.RETURN)
driver.save_screenshot('naver_login.jpg')

elements = driver.find_elements_by_tag_name('input')
print(type(elements))

for element in elements:
   if element.get_attribute('value') == '로그인':
        element.click()

driver.save_screenshot('naver_login2.jpg')
#driver.switch_to.frame('minime')
# a = driver.find_elements_by_tag_name('span')
# for b in a:
#    if b.get_attribute('class') == 'cnt':
#        print(b.text)