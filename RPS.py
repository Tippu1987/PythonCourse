import random

def Get_Options():
    options=["Rock","Paper","Scissors"]
    player_choice=random.choice(options)
    computer_choice=random.choice(options)
    return {"player":player_choice,"computer":computer_choice}

def Check_Winner(player, computer):
    print(f"Player Choice: {player}. Computer Choice: {computer}")
    if(player==computer):
        print(f"its a Tie..!")
    elif(player == "Rock"):
        if(computer == "Scissors"):
            print("Rock smashes Scissors. You Win!")
        else:
            print("Paper covers Rock. You lose.")
    elif(player == "Paper"):
        if(computer == "Rock"):
            print(f"Paper Covers Rock. You Win!")
        else:
            print(f"Scissors cuts paper. you lose")
    elif(player == "Scissors"):
        if(computer == "Paper"):
            print(f"Scissors cuts Paper. You Win!")
        else:
            print(f"Rock Smashes Scissors. You lose")

options=Get_Options()
Check_Winner(options["player"],options["computer"])




