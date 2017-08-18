from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
<<<<<<< HEAD
from settings.models import Profile
=======
>>>>>>> master
from skhufeeds import account

class UrlTokenBackend(ModelBackend):
    def authenticate(self, useruid, token):
        print("Authenticating user {} with token {}".format(useruid, token))
        user = User.objects.get(username = useruid)
        userInfo = Profile.objects.get(user = user)
        print(user, userInfo)
        if account.verifyToken(useruid, token):
            return user
        else:
            return None
