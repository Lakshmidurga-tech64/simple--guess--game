import random
guess_number=random.randint(1,5)
number=int(input("enter a number which lies in between 1 to 5:))
if(guess_number==number):
    print("you won the game")
else:
    print(f"you entered {number} doesn't match with computer number {guess_number})