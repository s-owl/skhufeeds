#성공회대학교 학생식당페이지 긁어오기
from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag


html = urlopen("http://www.skhu.ac.kr/uni_zelkova/uni_zelkova_4_3_view.aspx?idx=310")
bs0bj = BeautifulSoup(html.read(),"html.parser")


for child in bs0bj.find("table",{"class":"cont_c"}).tbody.children:
    if isinstance(child, Tag):
        item = child.findAll("td")
        print(item[0].get_text(),
        item[1].get_text(),
        item[2].get_text(),
        item[3].get_text(),
        item[4].get_text(),
        item[5].get_text())
