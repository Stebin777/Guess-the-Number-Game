import random

def difficulty_modes():
    while True:
        option = int(input("Selete the mode \n1. Easy(1–50) \n2. Medium (1–100) \n3. Hard (1–500) \n4. Back to menu \nEnter your choice "))
        if(option == 1):
            play(1,50)
            break
        elif(option == 2):
            play(1,100)
            break
        elif(option == 3):
            play(1,500)
            break
        elif(option == 4):
            break
        else:
            print("Invalid choice. Please try again.")


def play(a,b):
    random_number=random.randint(a,b)
    count=0
    print(f"Guess a number between {a} and {b}.")
    while True:
        user_number=int(input("Enter a number:"))
        count+=1
        if(user_number < a or user_number > b):
            print(f"Enter the number between{a}-{b}")
        elif(random_number == user_number):
            print("the number is",random_number)
            print( f"You guessed it in {count} attempts!")
            break
        elif(random_number < user_number):
            print("Too high!")
        elif(random_number > user_number):
            print("Too low!")
def custom_mode():
    play(int(input("Enter a number start:")),int(input("enter a number to end:")))

def main():
    while True:
        print("\nWelcome to the Guess the Number Game!")
        option = int(input("1. Difficulty Modes\n2. Custom Mode\n3. Exit\nEnter your choice: "))
        if(option == 1):
            difficulty_modes()
            print(" wants to play again.")
        elif(option == 2):
            custom_mode()
            print(" wants to play again.")
        elif(option == 3):
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            
main()
