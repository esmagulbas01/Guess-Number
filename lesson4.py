# decorater function
"""
def outer_function(name):
    def greeting():
        return f"Hello, {name}"
    return greeting()
print(outer_function("ali"))
#print(greeting("ali"))
#print(f"Hello,ali")







def decorator_function(func):
    def wrapper_function(*args,**kwargs):
        print(f"start")
        result=func(*args,**kwargs)
        print(f"end")
        return result
    return wrapper_function

@decorator_function
def myMessage():
    print("this is an example function")

myMessage()  
myMessage(k1=1,k2=3)
myMessage(1,2,3) 





def authentication(func):
    def wrapper(user,*args,**kwargs):
        if not user.get("auth",False):
            print("Authorization failed")
            return
        return func(user,*args,**kwargs)
    return wrapper
@authentication
def view_account(user):
    print(f"welcome,{user['name']}")

user1={"name":"ali","auth":False}
user2={"name":"veli","auth":True}

view_account(user1)
view_account(user2)





"""





def flexible_decorator(func):
    def wrapper(*args,**kwargs):
        print(f"fonksiyon adı:{func.__name__}")
        if(args):
            print(f"konumsal argümanlar:{args}")
        if(kwargs):
            print(f"anahtar değer argümanları:{kwargs}")
        result=func(*args,**kwargs)
        print(f"'{func.__name__}'fonksiyonunun sonucu: {result}\n")
        return result
    return wrapper
@flexible_decorator
def add(x,y):
    return x+y

@flexible_decorator
def greet(name,age,country):
    return f"merhaba {name},yaşın {age},ülken{country}"

@flexible_decorator
def multiple_and_sum(*numbers,factor):
    return sum(numbers)*factor

add(2,3)
greet("ali",age=34,country="türkiye")
multiple_and_sum(2,3,4,5,factor=8)



