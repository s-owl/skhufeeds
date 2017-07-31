#성공회대학교 대학기구_학생복지처 페이지 긁어오기
from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag

def run():
    html = urlopen("http://www.skhu.ac.kr/uni_int/uni_int_5_4.aspx")
    bs0bj = BeautifulSoup(html.read(),"html.parser")

    main = "대표전화 02)2610-4114 / 팩스 02)2683-8858/ 야간전화 02)2610-4119/ 직통전화 02)2610 + 교내번호"
    print(main)

    data = list()
    for child in bs0bj.find("table",{"class":"cont_a mt20 ml20 w690"}).tbody.children:
        if isinstance(child, Tag):
            item = child.findAll("td")
            data.append({"title":item[0].get_text(),
            "name":item[1].get_text(),
            "class":item[2].get_text(),
            "task":item[3].get_text(),
            "phone":item[4].get_text(),
            "fax":item[5].get_text() })

    return data
