from django.contrib.auth.models import User
import datetime, uuid
from jose import jwt

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
        # Generate Token
        print("Generating token for user {}.".format(useruid))
        newToken = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=3),
        'aud': user.username}, user.profile.secret)
        print(newToken)
        user.profile.token = str(newToken)
        user.save()
        return newToken

# Function that verifies token
# Returns True if verified, or False
# Returns None if other error(ex : user not found) has raised
def verifyToken(useruid, tokenToVerify):
    try:
        user = User.objects.get(username = useruid)
        # if(tokenToVerify == user.profile.token):
        print("NOW VERIFING.")
        jwt.decode(tokenToVerify, user.profile.secret, audience=useruid)
        print("TOKEN VERIFIED!")
        return True
        # else:
        #     print("VERIFICATION ERROR!")
        #     return False
    except User.DoesNotExist:
        print("Cannot find user {}.".format(useruid))
        return None
    except Exception as e:
        print(e)
        return None

    # except jwt.ExpiredSignatureError:
    #     print("SIGNATURE ERROR!")
    #     return False
    # except jwt.exceptions.InvalidAudienceError:
    #     print("TOKEN INVALID!")
    #     return False
    # except jwt.exceptions.DecodeError:
    #     print("DECODE ERRPR!")
    #     return False
