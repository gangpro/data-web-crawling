# 특정 url의 HTML을 읽어서 내용을 출력!!

from urllib.request import urlopen

# 특정 URL에 접속해서 접속객체를 생성
# urlObj = urlopen("http://localhost:8880/index.html")   # 개인 서버 test
urlObj = urlopen("http://www.naver.com/index.html")   # 실제 naver test


print(urlObj.read().decode("utf-8"))   #해당 URL에 대해 읽음