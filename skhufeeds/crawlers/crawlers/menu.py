#성공회대학교 대학기구_총무처 페이지 긁어오기
from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag

def run():
    html = urlopen("http://www.skhu.ac.kr/uni_zelkova/uni_zelkova_4_3_view.aspx?idx=310")
    bs0bj = BeautifulSoup(html.read(),"html.parser")

    data = list():

for child in bs0bj.find("table",{"class":"cont_c"}).tbody.children:
    if isinstance(child, Tag):
        item = child.findAll("td")
