# BeautifulSoup4 : HTML Parsing libarary   # HTML을 분석해서 추출하는 라이브러리

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://localhost:8880/index.html"
urlObj = urlopen(url)
bs = BeautifulSoup(urlObj.read(), "html.parser")

# find() 처음 찾은거 1개만 사용할 수 있다.   # 단점은 여러개 중에 1개만 찾는거?..
bs.find("h1")   #h1 tag만 찾아

# .text   .string   .get_text() : tag 사이의 문자열 추출하는 세가지 방법 다 동일하게 사용 가능
print(bs.find("h1").text)   #= 첫번째 h1
print(bs.find(id="cat").text)   #고유 식별자 id로 찾는 방법   #= 고양이
print(bs.find(class_="myStyle").text)   # class로 찾는 방법   #= 서울
print(bs.find(text="강아지").parent)   #= element를 찾을 때 .parent를 쓴다.   #= <li>강아지</li> 