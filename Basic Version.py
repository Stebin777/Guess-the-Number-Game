import random
a=1
b=100
random_number=random.randint(a,b)

while True:
    user_number=int(input("Enter a number:"))
    if(user_number < a or user_number > b):
        print(f"Enter the number between{a}-{b}")
    elif(random_number == user_number):
        print("the number is",random_number)
        break
    elif(random_number < user_number):
        print("Too high!")
        
    elif(random_number > user_number):
        print("Too low!")
