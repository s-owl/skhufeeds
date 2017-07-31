from django.contrib.auth.models import User
from settings.models import UserInfo
import jwt, datetime, uuid

def registerNewUser(useruid):
    userSecret = uuid.uuid4()

    newUser = User.objects.create_user(username=useruid, email=None, password=uuid.uuid4())
    newUser.save()

    newUserInfo = UserInfo()
    newUserInfo.user = newUser
    newUserInfo.last_pull = datetime.datetime.utcnow()
    newUserInfo.secret = userSecret
    newUserInfo.save()

    print("New user {} has been registered!".format(useruid))

def deleteUser(useruid):
    try:
        user = User.objects.get(username = useruid)
        user.delete()
        print("User {} has been deleted.".format(useruid))
    except User.DoesNotExist:
        print("Cannot find user {}.".format(useruid))
    except Exception as e:
        print(e)

# This function always returns new token for each user
def getToken(useruid):
    try:
        user = User.objects.get(username = useruid)
        userInfo = UserInfo.objects.get(user = user)
    except User.DoesNotExist:
        print("Cannot find user {}.".format(useruid))
        return None
    except Exception as e:
        print(e)
        return None
    else:
        # If UserInfo data exists, just save new token
        newToken = generateToken(useruid, userInfo.secret)
        userInfo.token = newToken
        userInfo.save()
        user.save()
        return newToken

def generateToken(useruid, secret):
    print("Generating token for user {}.".format(useruid))
    token = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
    'aud': useruid}, secret)
    print(token)
    return token


# Function that verifies token
# Returns True if verified, or False
# Returns None if other error(ex : user not found) has raised
def verifyToken(useruid, tokenToVerify):
    user = User.objects.get(username = useruid)
    userInfo = UserInfo.objects.get(user = user)
    if(tokenToVerify == userInfo.token):
        jwt.decode(tokenToVerify, userInfo.secret, audience=useruid)
        print("TOKEN VERIFIED!")
        return True
    else:
        print("VERIFICATION ERROR!")
        return False
