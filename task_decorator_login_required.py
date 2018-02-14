import hashlib

def make_token(username, password):
    s = username + password
    return hashlib.md5(s.encode()).hexdigest()

def login_required(func):
    def wrapper(*args, **kwargs):
        i = 0
        while i < 3 :
            login = input()
            password = input()
            with open('token.txt') as token:
                if make_token(login, password) != token.read():
                    i += 1
                else:
                    return func(*args, **kwargs)
        return None
    return wrapper

#@login_required
#def hello():
#    print("Hello world!")
#hello()
# with open('token.txt', 'w') as f:
#     f.write(make_token("username", "password"))
