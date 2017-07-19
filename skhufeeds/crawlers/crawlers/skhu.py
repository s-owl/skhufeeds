#성공회대학교 페이지 긁어오기
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.skhu.ac.kr/main.aspx")
bs0bj = BeautifulSoup(html.read(),"html.parser")
print(bs0bj.h1)

#예외처리
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs0bj = BeautifulSoup(html.read(), "html.parser")
        title = bs0bj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.skhu.ac.kr/main.aspx")
if title == None:
    print("Title could not be found")
else:
    print(title)
