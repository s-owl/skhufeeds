from . import util
from django.http import JsonResponse


def run(user, command, user_key):
    util.updateLastCommand(command,user.profile)
    return JsonResponse({
        'message' : {
            'text': '무엇으로 검색하시겠습니까?\n연락처는 내선번호와 이메일이 제공됩니다!'
        },
        'keyboard': {
            'type' : 'buttons',
            'buttons' : ['성명','소속','뒤로가기']
        }
    })
