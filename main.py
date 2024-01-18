from art import logo
import random

def random_number():
    return random.choice(range(1,101))

def guess_num_game(number, mode):
    if mode=="easy":
        chances=10
    else:
        chances=4
    
    while(chances>0):
        user_number=int(input("Guess the number: "))
        if user_number==number:
            return "win"
        elif user_number<number:
            print("Too low")
            chances-=1
            print(f"{chances} more tries")
        else:
            print("Too high")
            chances-=1
            print(f"{chances} more tries")
    return "lose"    
    
print(logo)

continue_game=True

while(continue_game):
    rand_num=random_number()
    
    game_mode=input("Type 'easy' if you want the easy mode, else type 'hard': ").lower()
    
    result=guess_num_game(rand_num, game_mode)
    
    print(f"You {result}")

    continue_game=False if input("Play again? (Y/N): ").lower() == 'n' else True

print("See you next time!")