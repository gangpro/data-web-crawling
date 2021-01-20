# BeautifulSoup4 : HTML Parsing libarary   # HTML을 분석해서 추출하는 라이브러리

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://localhost:8880/index.html"
urlObj = urlopen(url)
bs = BeautifulSoup(urlObj.read(), "html.parser")


# find_all() 조건에 맞는 element 값을 다 찾는다.
li_list = bs.find_all("li")   # 결과는 리스트로 리턴   # 한개를 찾아도 리스트 형태임

for li in li_list:
    print(li.text)   #= 호랑이, 강아지, 고양이, 서울, 부산, 제주



# find()를 사용 후 find_all() 사용하여 element 값의 조건에 맞는 것만 추출
li_list2 = bs.find("ul").find_all("li")

for li in li_list2:
    print(li.text)   #= 호랑이, 강아지, 고양이



# find_all() 사용하여 속성(href)의 값(http://....)을 추출
a_list = bs.find_all("a")   # a tag 찾기
for a in a_list:
    print(a.attrs["href"])   #= http://www.naver.com,   http://www.daum.com