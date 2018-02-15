import hashlib

user_authenticated = False

def make_token(username, password):
    s = username + password
    return hashlib.md5(s.encode()).hexdigest()

def login_required(func):
    def wrapper(*args, **kwargs):
        global user_authenticated
        if user_authenticated == False:
            i = 0
            while i < 3 :
                login = input()
                password = input()
                with open('token.txt') as token:
                    if make_token(login, password) != token.read():
                        i += 1
                    else:
                        user_authenticated = True
                        return func(*args, **kwargs)
            return None
        else:
            return func(*args, **kwargs)
    return wrapper

# @login_required
# def hello1():
#     print("The first function!!!")
# @login_required
# def hello2():
#     print("The second function!!!")
# @login_required
# def hello3():
#     print("The third function!!!")
# hello1()
# hello2()
# hello3()
# with open('token.txt', 'w') as f:
#     f.write(make_token("username", "password"))
