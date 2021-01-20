# 특정 url프로그램을 실행시켜서 결과를 가져오기!!(동적 데이터 가져오기)

from urllib.request import urlopen   #접속하기 위해 필요
from urllib.parse import urlencode   #

# 호출할 Open API의 url을 명시
# ex) 구글에서 영화진흥위원회 오픈 api 검색   # xml
# XML : http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=430156241533f1d058c603178cc3ca0e&targetDt=20120101
# URL 부분 : http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml
# param : key=430156241533f1d058c603178cc3ca0e     targetDt=20120101

open_api_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml"
open_api_param = {
    "key" : "430156241533f1d058c603178cc3ca0e",
    "targetDt" : "20190314"
}   # python dictionary 형태

url = open_api_url + "?" + urlencode(open_api_param)

urlObj = urlopen(url)

data = urlObj.read().decode("utf-8")
print(data)