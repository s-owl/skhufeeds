from django.contrib.auth.models import User
from skhufeeds.settings.models import UserInfo
import jwt, datetime

def registerNewUser(useruid):
    newUser = User.objects.create_user(useruid, None, None)
    newUser.save()
    print("New user {} has been registered!".format(useruid))

def deleteUser(useruid):
    try:
        user = User.objects.get(username = useruid)
        user.delete()
        print("User {} has been deleted.".format(useruid))
    except User.DoseNotExist:
        print("Cannot find user {}.".format(useruid))
    except Exception as e:
        print(e)

def getToken(userid):
    try:
        user = User.objects.get(username = useruid)
        userInfo = UserInfo.objects.get(user = user)
        return userinfo.token
    except User.DoseNotExist:
        print("Cannot find user {}.".format(useruid))
        return None
    except Exception as e:
        print(e)
        return None

def generateToken(userid):
    try:
        user = User.objects.get(username = useruid)
        userInfo = UserInfo.objects.get(user = user)
        # Generate Token that expires in a hour
        token = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(hour=1),
         'aud': userid}, user.password)
         # Save Token on DB
         userInfo.token = token
         userInfo.save()
        return token
    except User.DoseNotExist:
        print("Cannot find user {}.".format(useruid))
        return None
    except Exception as e:
        print(e)
        return None

# Function that verifies token
# Returns True if verified, or False
# Returns None if other error(ex : user not found) has raised
def vefiryToken(userid, tokenToVerify):
    try:
        user = User.objects.get(username = useruid)
        userInfo = UserInfo.objects.get(user = user)
        if(tokenToVerify == userInfo.token):
            jwt.decode(tokenToVerify, user.password, audience=userid)
            return True
        else:
            return False
    except User.DoseNotExist:
        print("Cannot find user {}.".format(useruid))
        return None
    except jwt.ExpiredSignatureError:
        return False
    except jwt.exceptions.InvalidAudienceError:
        return False
    excpet jwt.exceptions.DecodeError:
        return False
    except Exception as e:
        print(e)
        return None
