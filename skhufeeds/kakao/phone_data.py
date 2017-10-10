from crawlers.models import Contact
from pyexcel_xls import get_data
def save_to_db():
    data = get_data("skhufeeds_info.xls")  # 연락처가 저장된 엑셀파일 불러옴
    sheet = data['Sheet1']
    for i in range(2,len(sheet)):
        Contact.objects.get_or_create(
            name = sheet[i][1],
            desc = sheet[i][2],
            phone = sheet[i][3],
            email = sheet[i][4]
        )
    print("DONE!")
