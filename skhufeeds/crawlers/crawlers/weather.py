from urllib import request
import xml.etree.ElementTree as ET

opener = request.build_opener() # Init URL Opener
raw = opener.open("http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1153059500").read() # Load Data
tree = ET.fromstring(raw.decode("utf-8")) # Parse XML Doc
current = tree[0][6][5][1][0] # root - channel - item - description - body

# format current weather data
hour = current[0].text #시간
# day = items[1].text #day
temp = items[2].text #기온
condition = items[7].text #날씨상태
rain_prob = items[9].text #강수확률

today = tree[0][5].text

return """{} ~ {}:00 일기예보 \n
        현재 기온은 {}°C 이며, 날씨상태는 {}입니다\n
        비가 올 확률은 {}% 입니다""".format(today, hour, temp, condition, rain_prob)
