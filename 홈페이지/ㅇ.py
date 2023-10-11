import requests
from bs4 import BeautifulSoup

# 웹 페이지의 주소
url = "http://gs25.gsretail.com/gscvs/ko/store-services/locations"

# HTTP GET 요청을 보내고 응답 받기
response = requests.get(url)
html_content = response.text

# BeautifulSoup을 사용하여 HTML 코드 파싱
soup = BeautifulSoup(html_content, "html.parser")

# class가 "st_name"인 요소들을 모두 찾아 매장명 출력
store_names = soup.find_all(class_="st_name")

for store_name in store_names:
    print(store_name.get_text().strip())
