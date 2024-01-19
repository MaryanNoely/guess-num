from art import logo
from random import randint

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def random_number():
    return randint(0,100)

def set_difficulty():
    level=input("Type 'easy' if you want the easy mode, else type 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif level == "hard":
        return HARD_LEVEL_ATTEMPTS
    else:
        return 0

def guess_num_game(number, attempts):
    while(attempts>0):
        guess=int(input("Guess the number: "))
        if guess==number:
            return "win"
        elif guess<number:
            print("Too low")
            attempts-=1
            print(f"{attempts} more tries")
        else:
            print("Too high")
            attempts-=1
            print(f"{attempts} more tries")
    return "lose"    
    
print(logo)
continue_game=True
print("Welcome to the game!")

while(continue_game):

    answer=random_number()
    print("I'm thinking a number betwee 1 and 100")

    attempts=set_difficulty()
    if not attempts:
        print("Not an option, ending game")
        continue_game=False
        break 
    print(f"You have {attempts} attempts")

    result=guess_num_game(answer, attempts)
    
    print(f"You {result}")

    continue_game=False if input("Play again? (Y/N): ").lower() == 'n' else True

print("See you next time!")