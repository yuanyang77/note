import getpass

_username = "yy"
_passwd = "linfan"
error_user = []


count = 0
count2 = 0
while True:
    username = input("name: ")
    passwd = input("passwd: ")
    if username == _username and passwd == _passwd:
        print("login success!!")
        break
    elif username == _username and passwd != _passwd:
        print ("you passwd error!")
        count += 1
        if count == 3:
            error_user.append(username)
    else:
        print("you username error!")

    if username in error_user:
        print ("you user is look")
        break

