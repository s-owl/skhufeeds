#성공회대학교 학점교류 페이지 긁어오기
from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag

def run():
    url = "http://www.skhu.ac.kr/board/boardlist.aspx?bsid=10038&searchBun=89"
    html = urlopen(url)
    bs0bj = BeautifulSoup(html.read(),"html.parser")

    data = list()
    for child in bs0bj.find("div",{"id":"cont"}).table.tbody.children:
        if isinstance(child, Tag):
            item = child.find("td",{"class","left15"})
            title = item.get_text()
            link = "http://www.skhu.ac.kr/board/" + item.a['href']
            print(title,link)
            data.append({'title': title, 'url':link})

    return {
            "data": data,
            "source": {
                "name": "학점 교류 공지",
                "url": url,
                "desc": ""
                }
            }
