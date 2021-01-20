# BeautifulSoup4 : HTML Parsing libarary   # HTML을 분석해서 추출하는 라이브러리

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://localhost:8880/index.html"
urlObj = urlopen(url)
bs = BeautifulSoup(urlObj.read(), "html.parser")

# print(bs.html.body.div.ul.li.text)   # 다 써도 되지만 아래와같이 해도 됨.
print(bs.ul.li.text)  # 호랑이 찾기
print(bs.ul.li.next_sibling)   # 강아지 찾을 수 있을까? 하지만 공백때문에 못찾음.
print(bs.ul.li.next_sibling.next_sibling)   # 강아지


# <li id="tiger">호랑이</li>   => Element
# tag, attribute, text 개념이 있다. 