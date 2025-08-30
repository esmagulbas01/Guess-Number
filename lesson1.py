"""
colors = ["yellow","red","black"]
a,b,c = colors
print(a)
print(b)                                      #unpacking 
print(c)
"""

"""
x,y,z = "yellow","red","black"
print(x)
"""

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
name = "Ayşe "
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
x=["Ayşe","gul","Ahmet"]
y=["Ayşe","gul","Ahmet"]
z=x
print(x is z)
print(x is y)
print(x == y)
print(x is not z)
print(x is not y)
print(x != y)
print("Ayşe" in x)
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


"""
names=["Ayşe","gül","Ahmet"]
ages=[11,22,33]
print(list(zip(names,ages)))
"""

#    Comprehension
"""
fruit = ["grape","orange","strawberry","fig","kiwi","melon"]

[print(i) for i in fruit]

new_list=[item for item in fruit if("g" in item)]
print(new_list)


new_list2=[item.upper() for item in fruit if(item != "fig" )]
print(new_list2)


new_list3=[item if item!="kiwi" else "banana" for item in fruit]
print(new_list3)
"""
#(eğer kivi değilse yazdır kivi ise banana yazdır)



# Ternary operators
"""
a=int(input("Enter a integer:"))
b=int(input("Enter b integer:"))
print(f"{a} is greater than {b}") if(a>b) else print(f"{a} is less than {b}")

"""


#tuple değiştirilemez olduğundan veri ekleyemeyiz ama başka bir tuple ekleyebiliriz

"""
fruits = ("grape","orange","strawberry","fig","kiwi","melon")
extra=("plum",) # sonunda , oldupu için türü tupledır
fruits += extra
print(fruits)

"""

"""
fruits = ("grape","orange","strawberry","fig","kiwi","melon")
(x,y,*z)=fruits
print(fruits)
"""

"""
fruits = {"grape","orange","strawberry","fig","kiwi","melon"}
fruits2 = {"cherry","apple"}
fruits3={"pear","apple"}
fruits4=("apricot",)
fruits |= fruits2 | fruits3
fruits.update(fruits4)
fruits5 = fruits2 & fruits3
print(fruits)
print(fruits5)
"""




"""
def my_function(*args):
    print(args[2])

my_function("ali","murat","nazlı") 
"""


"""
x="awesome"
def my_function():
    x="fantastic"
    print(f"python is {x}")

my_function()
print(f"python is {x}")
"""   

"""
def my_function():
    global x
    x="fantastic"
    print(f"python is {x}")

my_function()
print(f"python is {x}")
"""

