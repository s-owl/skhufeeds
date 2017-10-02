#성공회대학교 대학기구-교무처 페이지 긁어오기
from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag

def run():
    html = urlopen("http://www.skhu.ac.kr/uni_int/uni_int_5_2.aspx") #성공회대학교 대학기구-교무처 url
    bs0bj = BeautifulSoup(html.read(),"html.parser")

    #공통된 번호 저장 및 출력
    main = "대표전화 02)2610-4114 / 팩스 02)2683-8858 / 야간전화 02)2610-4119 / 직통전화 02)2610 + 교내번호"
    print(main)

    # for문을 사용하여 원하는 부분을 추출 및 출력
    data = list()
    for child in bs0bj.find("table",{"class":"cont_a mt20 ml20 w690"}).tbody.children:
        if isinstance(child, Tag): #child의 타입이 Tag인지 확인
            item = child.findAll("td")
            data.append({"title":item[0].get_text(), #소속
            "name":item[1].get_text(), #이름
            "class":item[2].get_text(), #직책
            "task":item[3].get_text(), #담당업무
            "phone":item[4].get_text(), #내선번호
            "fax":item[5].get_text() }) #fax번호
    return data
