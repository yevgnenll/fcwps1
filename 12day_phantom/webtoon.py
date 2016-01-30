from bs4 import BeautifulSoup, Tag
import requests


def download_webtoon(url, path):
    """
    naver webtoon의 이미지를 내가 원하는 폴더에 다운받는다
    :param url: 원하는 웹툰 url
    :param path: 다운받는 절대경로
    """
    html_res =requests.get(url)

    html = BeautifulSoup(html_res.content, "html.parser")

    result = str(html.find_all('img', attrs={"alt":"comic content"})[0]).split(">")
    webtoon = str(result).split(" ")

    img_src = list()
    for idx, src in enumerate(webtoon):
        if src.startswith("src"):
            img_src.append(src[5:-1])

    header = {'Referer':url+'&listPage=1&mobile=y'}

    for source in img_src:
        fileName = str(source).split("/")[-1]
        with open(path+fileName, "wb") as fout:
            response = requests.get(source, stream=True,headers =header)
            # allow_redirects, stream, headers
            fout.write(response.content)


download_webtoon("http://comic.naver.com/webtoon/detail.nhn?titleId=616239&no=197&weekday=tue","/Users/yevgnenll/Desktop/comic/")
