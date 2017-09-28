from django.http import JsonResponse
from . import util

cmd = '연락처'

def run():
    util.updateLastCommand(command,user.profile)
    return JsonResponse({
        'message' : {
            'text': '무엇으로 검색하시겠습니까?\n연락처는 내선번호와 이메일이 제공됩니다.\n아직 등록되지 않은 전화번호와 이메일이 있을 수 있습니다.'
        },
        'keyboard': {
            'type' : 'buttons',
            'buttons' : ['성명','소속']
        }
    })
