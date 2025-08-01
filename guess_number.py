import random
random_number= random.randint(1,100)
remaining_attemp =10
score=100
attemp_count=0
print(f"Your starting score: {score}")
print("Guess a number between 1 and 100")

while (remaining_attemp>0):
    predicted_number=int(input("predicted number:"))
    attemp_count+=1
    if not(predicted_number<101 and predicted_number>0):
        print("Please!Enter a number between 1 and 100 ")
        continue
    if(predicted_number==random_number):
        print(f"You guessed the number correctly on your {attemp_count}.attempt")
        print(f"Your total score {score}")
        break
    elif(predicted_number<random_number):
        print("guess a larger number")
    else:
        print("guess a smaller number")

    remaining_attemp-=1
    score-=15
    
    if(remaining_attemp>0):
        print(f"Remining attempts:{remaining_attemp}")
        print(f"current score:{score}")
    else:
        print(f"Unfortunately! You ran out of atttemptd")
        print(f"Your total score:{score}")    

print("try again")    

    
