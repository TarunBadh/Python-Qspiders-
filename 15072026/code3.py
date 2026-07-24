#29. Wap to login into the Instagram with valid username and password. (enter password only if the user name is valid)
# WAP to login into Instagram with valid username and password
Valid_username=input('Enter the username : ')
Valid_password = input('Enter the Password : ')
print('-------- Instagram Login---------')
username = input('Enter the Username : ')
if Valid_username==username :
    password =input('Enter the password :  ')
    if password == Valid_password:
        print('Login Successfully')
    else : 
        print('Incorrect Password')
else :
    print('Invalid username')