# BeautifulSoup4 : HTML Parsing libarary   # HTML을 분석해서 추출하는 라이브러리

from urllib.request import urlopen
from bs4 import BeautifulSoup

# 로튼토마토 영화 정보
url = "https://www.rottentomatoes.com/top/bestofrt/?year=2018"
urlObj = urlopen(url)
bs = BeautifulSoup(urlObj.read(), "html.parser")


tr_list = bs.select("#top_movies_main > div > table > tr")

result = []
for tr in tr_list:
    result.append(tr.select_one("td:nth-of-type(3) > a").text.strip())


# TOP 100 MOVIES OF 2018
print(result)