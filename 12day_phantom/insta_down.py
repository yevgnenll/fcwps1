# -*- encoding : utf-8 -*-
from selenium import webdriver
from urllib.parse import quote
import requests

def downImageInsta(hashword, filepath):
    """
    insta에서 해쉬태그 검색 결과의 이미지를 다운로드함
    :param hashword: 해쉬태그 검색어
    :param filepath: 다운받을 경로
    :return: 없음.
    """
    url = 'https://www.instagram.com/explore/tags/'+quote(hashword.encode('utf-8'))
    offset = 0
    driver = webdriver.PhantomJS('/usr/local/lib/node_modules/phantomjs/bin/phantomjs')
    driver.get(url)

    result = list()
    isFirst = False #최초 한번
    offset_mid = 0
    while True:

        while True:
            try:
                image = driver.find_element_by_id("pImage_"+str(offset)).get_attribute("src")
                result.append(image)
            except:
                break
            finally:
                if len(result) == 0:
                    print("검색결과가 없거나 아직 반영되지 않음")
            offset += 1
            if((offset+1)%12 == 0):
                break

        for i in range(offset_mid, offset):
            with open(filepath+hashword+"_"+str(i)+".jpg", "wb") as fout:
                response = requests.get(result[i], stream=True) #image
                fout.write(response.content)
        offset_mid = offset
        more = input("더 읽어들일까요? (yes/no)")

        if (more == "yes" or more == "y") and not isFirst:
            driver.find_element_by_class_name(" _1ooyk").click()
            driver.save_screenshot("insta.jpg")
            isFirst = True
        elif (more =="yes" or more=="y") and isFirst:
            print(offset)
        else:
            driver.quit()
            break


downImageInsta("cake", "/Users/yevgnenll/Desktop/comic/")


