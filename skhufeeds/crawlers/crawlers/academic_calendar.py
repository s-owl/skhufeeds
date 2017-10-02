#성공회대학교 학사일정 페이지 긁어오기
from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag

def run():
    html = urlopen("http://www.skhu.ac.kr/calendar/calendar_list_1.aspx") #성공회대학교 학사일정 url
    bs0bj = BeautifulSoup(html.read(),"html.parser")

    data = "" #변수 선언 및 초기화

    # for문을 사용하여 원하는 부분을 추출 및 출력
    for child in bs0bj.find("div",{"class","info"}).table.tbody.children:
        if isinstance(child, Tag):#child의 타입이 Tag인지 확인
            date = child.find("td",{"class","day"}) #날짜
            contents = child.find("td",{"class","txt"}) #내용
            if isinstance(date, Tag):#child의 타입이 Tag인지 확인
                data+="[{}] {}\n".format(date.get_text(), contents.get_text()) #날짜와 행사내용
    return data 
