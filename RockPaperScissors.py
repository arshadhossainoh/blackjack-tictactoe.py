import random


def who_wins():
    
    if user == "rock":
        if computer == "rock":
            print("its a tie")
        elif computer == "paper":
            print("computer wins")
        elif computer == "scissors":
            print("user wins")
    elif user == "paper":
        if computer == "rock":
            print("user wins")
        elif computer == "paper":
            print("its a tie")
        elif computer == "scissors":
            print("computer wins")
    elif user == "scissors":
        if computer == "rock":
            print("computer wins")
        elif computer == "paper":
            print("user wins")
        elif computer == "scissors":
            print("its a tie")

    print(f"user picked {user} & computer picked {computer}")




game_over = False
while not game_over:
    option = ["rock", "paper", "scissors"]
    user = input("'rock', 'paper' or 'scissors' ? \n")
    computer = random.choice(option)
    who_wins()
    
    play_agian = input("wanna play again Y or N : \n")
    if play_agian == "N":
        game_over = True
        print("thanks for playing, bye")
    


    



