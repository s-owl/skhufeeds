from django.contrib.auth.backends import ModelBackend
from settings.models import UserInfo
import jwt

class UrlTokenBackend(ModelBackend):
    def authenticate(self, useruid, token):
        try:
            user = User.objects.get(username = useruid)
            userInfo = UserInfo.get(user = user)
            if(userInfo.token == token):
                jwt.decode(token, user.password, audience=useruid)
                return user
