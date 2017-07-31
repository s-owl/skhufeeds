#성공회대학교 학사일정 페이지 긁어오기
from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag

def run():
    html = urlopen("http://www.skhu.ac.kr/board/boardlist.aspx?bsid=10008")
    bs0bj = BeautifulSoup(html.read(),"html.parser")

    data = list():

    for child in bs0bj.find("div",{"class","info"}).table.tbody.children:
        if isinstance(child, Tag):
            date = child.find("td",{"class","day"})
            contents = child.find("td",{"class","txt"})
            if isinstance(date, Tag):
                print(date.get_text(), contents.get_text())
                data.append({"1":"date","2":"contents"})
        return data
