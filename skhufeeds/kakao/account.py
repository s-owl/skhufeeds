from django.contrib.auth.models import User

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
