# 특정 url의 HTML을 읽어서 내용을 출력!!

from urllib.request import urlretrieve

# 저장하려는 resource에 대한 url을 지정
url = "http://www.naver.com/index.html"

# 저장하려는 경로와 파일명을 명시
save_file = "../naver.index.html"   # ../ 상위폴더를 의미

urlretrieve(url,save_file)   #

print("성공적으로 저장되었음!!")