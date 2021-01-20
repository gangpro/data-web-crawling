# BeautifulSoup4 : HTML Parsing libarary   # HTML을 분석해서 추출하는 라이브러리

from urllib.request import urlopen
from bs4 import BeautifulSoup

# 네이버 금융 환율 가져오기.
url = "https://finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_USDKRW"
urlObj = urlopen(url)
bs = BeautifulSoup(urlObj.read(), "html.parser")

# 구글 크롬에서 해당 사이트 F12 키를 누르면 개발자 창이 뜸.
# Commanc+Shift+C : 내가 원하는 위치의 정보 추적하여 코드 정보를 알 수 있음.
# 원달러 정보가 있는 span의 부모 element인 em에서 오른쪽 마우스 클릭
# copy - copy selector 하면 아래와 같이 정보 복사 됨.
#content > div.spot > div.today > p.no_today > em > em

em = bs.select_one("#content > div.spot > div.today > p.no_today > em > em")
print(em)

result = []
for item in em.select("span"):
    result.append(item.text)

print("오늘의 원달러 환율은 : {}".format("".join(result)))


