from getpass import getpass
isLogin = False
loginAttempt = 0 

u = "user1"
p = "SSNA"

while isLogin == False:

    username = input("Input USERNAME: ")
    password = getpass("Input PASSWORD: ")

    if username == u and password == p:
        print("Login Successful ")
        print("Login attempt: ", loginAttempt)
        isLogin = True
    else: 
        print("Incorrect Username and Password \nPlease Log in again")
        loginAttempt += 1
        isLogin = False