defaultBtns = ['학교소식','연락처','학사일정','날씨','학식','설정']

def updateLastCommand(command, userInfo):
    userInfo.last_input = command
    userInfo.save()
