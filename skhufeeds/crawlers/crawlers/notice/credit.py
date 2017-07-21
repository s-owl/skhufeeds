#성공회대학교 학점교류 페이지 긁어오기
from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag
html = urlopen("http://www.skhu.ac.kr/board/boardlist.aspx?bsid=10038&searchBun=89")
bs0bj = BeautifulSoup(html.read(),"html.parser")
# print(bs0bj.h1)


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.skhu.ac.kr/board/boardlist.aspx?bsid=10038&searchBun=89")
bj0bj = BeautifulSoup(html, "html.parser")

for child in bs0bj.find("div",{"id":"cont"}).table.tbody.children:
    # item = child.contents[1]
    if isinstance(child, Tag):
        item = child.find("td",{"class","left15"})
        title = item.get_text()
        link = "http://www.skhu.ac.kr/board/" + item.a['href']
        print(title,link)
