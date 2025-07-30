colors = ["yellow","red","black"]
a,b,c = colors
print(a)
print(b)                                      #unpacking 
print(c)


x,y,z = "yellow","red","black"
print(x)


"""
test = "marvellous"


def myFuntion():
    test = "fantastic"
    print(test)

myFuntion()
print(test)
"""

"""
def myFunction():
    global x
    x = "fantastic"
    

myFunction()
print(x)
"""



"""
name = "Esma "
age = 24
example1 = f"My name is {name}and l am {age}"
#example1="My name is {0} and l am {1} years old ".format(name,age)
print(example1)



example2 = "This prices is only {price:.2f} Turkish Lira"
print(example2.format(price=73.5432))

"""


"""

score=int(input("Bir sayı girin:"))
if not(score<50):
    print("Successful")
else:
    print("fail")

"""



"""
x=["esma","gul","bas"]
y=["esma","gul","bas"]
z=x
print(x is z)
print(x is y)
print(x == y)
print(x is not z)
print(x is not y)
print(x != y)
print("esma" in x)
print("ayse" not in x)

"""


"""
for i in range(5):                     # çıktıyı aynı satırda yazdırmak için
    print(i ,end= " ")
    
"""

"""

for item in range(8):
    if(item==5):
        pass
    else:
        print(item)
        
"""



"""
my_numbers=[[2,3],[4,5],[6,7]]

for item1,item2 in my_numbers:
    print(f"{item1},{item2}")
    
"""

"""
numbers=[44,55,66]
for index,num in enumerate(numbers):
    print(f"{index}-{num}")
    
"""


names=["esma","gül","bas"]
ages=[11,22,33]
print(list(zip(names,ages)))