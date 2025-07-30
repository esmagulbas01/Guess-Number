a = "Methods in Python"
b=a.split()
m=''
total=0
for i in b:
    if len(i) > total:                                     
        m=i
        total = len(i)  
print(total , m)  
