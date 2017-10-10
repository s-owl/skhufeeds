#성공회대학교 학생식당_식단안내 페이지 긁어오기
from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag
from crawlers.models import Diet
from django.utils import timezone
from datetime import datetime

def run():
    html = urlopen("http://skhu.ac.kr/uni_zelkova/uni_zelkova_4_3_list.aspx")#성공회대학교 학생식단표 게시판 접근
    bs0bj = BeautifulSoup(html.read(),"html.parser")
    for child in bs0bj.find("div",{"id":"cont"}).table.tbody.children: #학식 게시판에서 학식이 나와있는 항목으로 접근하기
        if isinstance(child, Tag): #child의 타입이 Tag인지 확인
            item = child.find("td",{"class","left15"}) #게시판 목록을 가져오기
            link = "http://skhu.ac.kr/uni_zelkova/{}".format(item.a['href']) # 목록으로 가는 링크

    html = urlopen(link) #학식 최신 식단표 접근
    bs0bj = BeautifulSoup(html.read(),"html.parser")

    data = list()
    date = list()
    #for문을 사용하여 날짜 뽑아오기
    for child in bs0bj.find("tr",{"class":"item_th"}).children:
        if isinstance(child,Tag):
            date.append(child.get_text())
    data.append(list(filter(lambda x: x != "일자", date)))
    del data[0][0]

    # for문을 사용하여 식단내용 추출 및 출력
    for child in bs0bj.find("div",{"class":"box_menu_in"}).table.tbody.children:
        if isinstance(child, Tag): #child의 타입이 Tag인지 확인
            corner = list()
            item = child.findAll("td")
            for i in range(0,6):
                corner.append(item[i].get_text("\n"))
            data.append(corner)
    print(data)
    #요일별 식단 저장
    for i in range(0, 5):
        if(data[0][i] != ""):
            Diet.objects.get_or_create(
                date = timezone.make_aware(datetime.strptime(data[0][i],'%Y-%m-%d')),
                lunchA = data[1][i],
                lunchB = data[3][i],
                dinner = data[7][i]
            )
