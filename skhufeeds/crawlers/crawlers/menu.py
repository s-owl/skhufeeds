#성공회대학교 학생식당_식단안내 페이지 긁어오기
from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag
from crawlers.models import Diet

def run():
    html = urlopen("http://skhu.ac.kr/uni_zelkova/uni_zelkova_4_3_list.aspx")#성공회대학교 학생식당 식단안내 url
    bs0bj = BeautifulSoup(html.read(),"html.parser")
    data = list()
    date = list()
    #for문을 사용하여 날짜 뽑아오기
    for child in bs0bj.find("tr",{"class":"item_th"}).children:
        if isinstance(child,Tag):
            date.append(child.get_text())
    date.remove("일자")
    data.append(date)

    # for문을 사용하여 식단내용 추출 및 출력
    for child in bs0bj.find("div",{"class":"box_menu_in"}).table.tbody.children:
        if isinstance(child, Tag): #child의 타입이 Tag인지 확인
            corner = list()
            item = child.findAll("td")
            for i in range(0,6):
                corner.append(item[i])
            data.append(corner)
    #요일별 식단 저장
    for i in range(0,6):
        diet, created = text.objects.get_or_create(
            date = datetime.datetime.strptime('2017-09-25','%Y-%m-%d').date()
            lunchA = data[1][i],
            lunchB = data[2][i],
            dinner = data[3][i]
        )
        diet.save()


run()
