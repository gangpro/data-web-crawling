# BeautifulSoup4 : HTML Parsing libarary   # HTML을 분석해서 추출하는 라이브러리

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://localhost:8880/index.html"
urlObj = urlopen(url)
bs = BeautifulSoup(urlObj.read(), "html.parser")

# HTML 내에서 내가 원하는 값 한개 찾기   # 일반적으로 아이디를 찾음. 왜? 한개니깐. 아하.
# ex) 아이디가 tiger인걸 찾기
# "#tiger" : 여기서 "" 안에 #은 아이디를 의미 함.
print(bs.select_one("#tiger"))        #= <li id="tiger">호랑이</li>
print(bs.select_one("#tiger").text)   #= 호랑이

# tag를 찾을 땐 tag name을 그대로 쓴다.
# "ol"의 "li" 자식 값 찾기
# 그 중에(nth) - 두번째 자식(child(2)
# bs.select_one("ol > li:nth-child(2)") 정석 표현 방식
# bs.select_one("ol > li:nth-of-type(2)") #BeautifulSoup4 표현 방식
print(bs.select_one("ol > li:nth-of-type(2)").text)   #= 부산

# HTML 내에서 내가 원하는 값 여러개 찾기
# 결과값은 list로 return
for li in bs.select("li"):
    print(li.text)     #= [호랑이, 강아지, 고양이, 서울, 부산, 제주]


