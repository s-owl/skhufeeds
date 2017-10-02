from urllib import request
import xml.etree.ElementTree as ET

def run(time_range):
    opener = request.build_opener() # Init URL Opener
    raw = opener.open("http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1153059500").read() # Load Data
    tree = ET.fromstring(raw.decode("utf-8")) # Parse XML Doc
    current = tree[0][6][5][1] # root - channel - item - description - body
    today = tree[0][5].text
    weather = "{} 일기예보\n".format(today)

    for i in range(0, time_range):
        # format current weather data
        hour = current[i][0].text #시간
        # day = items[1].text #day
        temp = current[i][2].text #기온
        condition = current[i][7].text #날씨상태
        rain_prob = current[i][9].text #강수확률
        weather += "{}시 - {}°C {} 강수확률: {}% 입니다.\n\n".format(hour,temp,condition,rain_prob)

    return weather
