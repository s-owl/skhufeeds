#성공회대학교 학사일정 페이지 긁어오기
from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag
html = urlopen("http://www.skhu.ac.kr/calendar/calendar_list_1.aspx")
bs0bj = BeautifulSoup(html.read(),"html.parser")
# print(bs0bj.h1)


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.skhu.ac.kr/calendar/calendar_list_1.aspx")
bj0bj = BeautifulSoup(html, "html.parser")

for child in bs0bj.find("div",{"class","info"}).table.tbody.children:
    if isinstance(child, Tag):
        date = child.find("td",{"class","day"})
        contents = child.find("td",{"class","txt"})
        if isinstance(date, Tag):
            print(date.get_text(), contents.get_text())
