from django.contrib.auth.models import User
import jwt, datetime, uuid

def registerNewUser(useruid):
    userSecret = uuid.uuid4()

    newUser = User.objects.create_user(username=useruid, email=None, password=uuid.uuid4())
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
        tokenStr = str(generateToken(useruid, user.profile.secret))
        user.profile.token = tokenStr.replace("'", ":") # Replace single quote with colon
        user.save()
        return tokenStr

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
    try:
        user = User.objects.get(username = useruid)
        if(tokenToVerify.replace("'", ":") == user.profile.token):
            jwt.decode(tokenToVerify, user.profile.secret, audience=useruid)
            print("TOKEN VERIFIED!")
            return True
        else:
            print("VERIFICATION ERROR!")
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
