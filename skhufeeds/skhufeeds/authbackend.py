from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from settings.models import UserInfo
from skhufeeds import account
import jwt

class UrlTokenBackend(ModelBackend):
    def authenticate(self, useruid, token):
        print("Authenticating user {} with token {}".format(useruid, token))
        user = User.objects.get(username = useruid)
        userInfo = UserInfo.objects.get(user = user)
        print(user, userInfo)
        if account.verifyToken(useruid, token):
            return user
        else:
            return None
