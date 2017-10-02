#성공회대학교 행사공지 페이지 긁어오기
from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag

def run():
    url = "http://www.skhu.ac.kr/board/boardlist.aspx?bsid=10008" #성공회대학교 행사공지 url
    html = urlopen(url)
    bs0bj = BeautifulSoup(html.read(),"html.parser")

    data = list()
    for child in bs0bj.find("div",{"id":"cont"}).table.tbody.children:
        if isinstance(child, Tag): #child의 타입이 Tag인지 확인
            item = child.find("td",{"class","left15"}) #게시판 목록 가져오기
            title = item.get_text() #게시판 목록 제목 가져오기
            link = "http://www.skhu.ac.kr/board/" + item.a['href'] #목록으로 가는 링크 가져오기
            print(title,link) #제목과 링크 출력하기
            data.append({'title': title, 'url':link})

    return {#DB에 저장하기위해 딕셔너리로 반환
            "data": data,
            "source": {
                "name": "행사 공지",
                "url": url,
                "desc": ""
                }
            }
