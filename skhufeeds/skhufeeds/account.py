from django.contrib.auth.models import User
import jwt, datetime, uuid, re

def registerNewUser(useruid):
    userSecret = uuid.uuid4()

    newUser = User.objects.create_user(useruid, None, None)
    newUser.set_unusable_password()
    newUser.save()

    newUser.profile.last_pull = datetime.datetime.utcnow()
    newUser.profile.secret = userSecret
    newUser.save()

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
    except User.DoesNotExist:
        print("Cannot find user {}.".format(useruid))
        return None
    except Exception as e:
        print(e)
        return None
    else:
        # If UserInfo data exists, just save new token
        user.profile.token = re.escape(generateToken(useruid, user.profile.secret))
        user.save()
        return user.profile.token

def generateToken(useruid, secret):
    print("Generating token for user {}.".format(useruid))
    return jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
    'aud': useruid}, secret)


# Function that verifies token
# Returns True if verified, or False
# Returns None if other error(ex : user not found) has raised
def verifyToken(useruid, tokenToVerify):
    try:
        user = User.objects.get(username = useruid)
        if(tokenToVerify == user.profile.token):
            jwt.decode(tokenToVerify, user.profilesecret, audience=useruid)
            return True
        else:
            return False
    except User.DoesNotExist:
        print("Cannot find user {}.".format(useruid))
        return None
    except jwt.ExpiredSignatureError:
        return False
    except jwt.exceptions.InvalidAudienceError:
        return False
    except jwt.exceptions.DecodeError:
        return False
    except Exception as e:
        print(e)
        return None
