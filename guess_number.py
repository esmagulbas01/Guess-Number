import random
number= random.randint(1,100)
One_attemp =10
start_score=100

print(f"your start score: {start_score}")
print("Guess a number")

while (One_attemp>0):
    predicted_number=int(input("predicted number:"))
    if not(predicted_number<101 and predicted_number>0):
        continue
    if(predicted_number==number):
        print("true guess")
        break
    elif(predicted_number<number):
        print("guess a larger number")
    else:
        print("guess a smaller number")

    One_attemp = One_attemp-1
    start_score= start_score -15
    
    print(f"new score:{start_score}")

print("try again")    

    
