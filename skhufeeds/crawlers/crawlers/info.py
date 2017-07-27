#성공회대학교 대학기구 페이지 긁어오기
from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag
html = urlopen("http://www.skhu.ac.kr/uni_int/uni_int_5_2.aspx")
bs0bj = BeautifulSoup(html.read(),"html.parser")


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.skhu.ac.kr/uni_int/uni_int_5_2.aspx")
bj0bj = BeautifulSoup(html, "html.parser")

main = "대표전화 02)2610-4114 / 팩스 02)2683-8858 / 야간전화 02)2610-4119"
print(main)


for child in bs0bj.find("table",{"class":"cont_a mt20 ml20 w690"}).tbody.children:
    if isinstance(child, Tag):
        item = child.findAll("td")
        print(item[0].get_text() ,item[1].get_text(),item[2].get_text(),item[3].get_text(),item[4].get_text(),item[5].get_text())
