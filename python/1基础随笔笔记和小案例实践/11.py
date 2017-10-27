arr = ['user:pwd','user1:pwd1','user2:123']

str_user = raw_input('input username:')
str_pwd = raw_input('input pwd:')
str_login = ':'.join([str_user,str_pwd])
if str_login in arr:
    print 'login sucess!'
for x in arr:
    if str_user not in x and str_pwd in x:
        print 'login username error'
        break
    elif str_pwd not in x and str_user in x:
        print 'login pwd error!'
        break
    else:
        print 'login username and pwd both error'
        break
