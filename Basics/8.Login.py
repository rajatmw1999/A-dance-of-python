import hashlib

users = {}

def CreateUser(username, password):
    try:
        if username in users:
            # existing_user = users[username]
            print("User is already present")
        else:
            users[username] = password
        print(users)
    except Exception as e:
        print(e)
        return {"statusCode":500, "message":e}

def CheckPassword(username, password):
    try:
        if username in users:
            if password == users[username]:
                print("You are logged in!")
                return True
            else:
                print("Wrong Password")
        return False
    except Exception as e:
        print("Error")
        print(e)
        return {"statusCode":500, "message":e}

def UpdatePassword(username, oldpassword, newpassword):
    try:
        if CheckPassword(username,oldpassword) == True:
            users[username] = newpassword
            print("Password Updated")
        else:
            print("Wrong password")
    except Exception as e:
        print("Error")
        print(e)
        return {"statusCode":500, "message":e}

def Encrypt(password):
    try:
        hashedpassword = hashlib.sha224(password.encode()).hexdigest()
        print(hashedpassword)
    except Exception as e:
        print("Error")
        print(e)
        return {"statusCode":500, "message":e}


CreateUser('ayan','password')
CreateUser('ayan2','password')
CreateUser('ayan3','password')
CheckPassword('ayan','password')
CheckPassword('ayan2','pafgssword')
CheckPassword('ayan3','peassword')
UpdatePassword('ayan3','password', 'mypassword')
print("--------")
CheckPassword('ayan3','mypassword')
CheckPassword('ayan3','mypassworderf23f')
# Encrypt("newpassword")
# 323894732948
# Creditcard#$23456
# f2c57870308dc87f432e5912d4de6f8e322721ba