#성공회대학교 장학공지 페이지 긁어오기
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.skhu.ac.kr/board/boardlist.aspx?bsid=10006&searchBun=75")
bs0bj = BeautifulSoup(html.read(),"html.parser")
print(bs0bj.h1)

#트리이동
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.skhu.ac.kr/board/boardlist.aspx?bsid=10006&searchBun=75")
bj0bj = BeautifulSoup(html, "html.parser")

for child in bs0bj.find("div",{"id":"cont"}).table.tbody.children:
    print(child)
