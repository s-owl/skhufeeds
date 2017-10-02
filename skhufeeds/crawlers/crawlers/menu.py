#성공회대학교 학생식당_식단안내 페이지 긁어오기
from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag

def run():
    html = urlopen("http://www.skhu.ac.kr/uni_zelkova/uni_zelkova_4_3_view.aspx?idx=315")#성공회대학교 학생식당 식단안내 url
    bs0bj = BeautifulSoup(html.read(),"html.parser")
    data = list()

    # for문을 사용하여 원하는 부분을 추출 및 출력
    for child in bs0bj.find("div",{"class":"box_menu_in"}).table.tbody.children:
        if isinstance(child, Tag): #child의 타입이 Tag인지 확인
            item = child.findAll("td")
            print(item[0].get_text("\n"), #학생식단 출력
            item[1].get_text("\n"),
            item[2].get_text("\n"),
            item[3].get_text("\n"),
            item[4].get_text("\n"),
            item[5].get_text("\n"))
