from crawlers.models import Contact
from pyexcel_xls import get_data
def save_to_db():
    data = get_data("skhufeeds_info.xls")
    sheet = data['Sheet1']
    for i in range(2,len(sheet)):
        item = Contact.objects.create()
        item.name = sheet[i][1]
        item.desc = sheet[i][2]
        item.phone = sheet[i][3]
        item.email = sheet[i][4]
        item.save()
    print("DONE!")
