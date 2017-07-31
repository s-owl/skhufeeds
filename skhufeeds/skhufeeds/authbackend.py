from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from settings.models import UserInfo
import jwt

class UrlTokenBackend(ModelBackend):
    def authenticate(self, useruid, token):
        user = User.objects.get(username = useruid)
        userInfo = UserInfo.objects.get(user = user)
        if(userInfo.token == token):
            jwt.decode(token, user.password, audience=useruid)
            return user
