import random

print("Rules of the Rock paper scissor game Super Heroes edition: \n"
                                +"Spiderman vs Storm or Green Lantern -> Spiderman wins \n"
                                + "Wonder Woman vs Spiderman or Hulk -> Wonder Woman wins \n"
                                +"Storm vs Wonder Woman or Hulk -> Storm wins \n"
                                + "Green Lantern vs Wonder Woman or Storm -> Green Lantern wins \n"
                                + "Hulk vs Spiderman or Green Lantern -> Hulk wins \n") 

heroes = ["spiderman", "storm", "green lantern", "wonder woman", "hulk"]
# Creating a dictionary with the heroes and the battles.
battle_result = {
    "spiderman": [ {"green lantern": "Steals Green Lanterns Ring"},
                    {"storm" : "Entangles Storm in a web"}
                    ],

    "wonder woman": [ {"spiderman": "Crushes Spiderman"},
                        {"hulk": "Smacks Hulk into last week"}],

    "storm": [ {"wonder woman": "Projects a tornado against Wonder Woman"},
                {"hulk": "Beats Hulk in a fair fight"}],
    "green lantern": [{"wonder woman": "Traps Wonder Woman in Pocket dimension"},
                        {"storm": "Removes Storm Gauntlet and beats her with it"}],
    "hulk": [{"spiderman": "Smashes Spiderman"},
            {"green lantern": "Sucker punches Green Lantern"}]
}

player = False
#Choosing the number of round the user wants to play.
num = int(input("Please enter the number of rounds: "))

if(num%2==0):
    num += 1

player_score = 0
computer_score = 0
total_round = num
    
playAgain = True

#Creating the loop, computer and user choose the hero.
while (playAgain):
    while(num > 0):

        print(f"\t\tROUND NUMBER :  {total_round - num + 1}")

        computer = random.choice(heroes).lower()
        print("Choose your Hero: Spiderman, Wonder Woman, Storm, Green Lantern, Hulk")
        player = input("Select a Hero: ").lower()
        print("player choice is:" + player)
        print("\nNow its computer turn.....")
        print("computers choice is: " + computer)
        print(player + " V/s " + computer)

        if computer == player:
            print(f" Draw {total_round - num + 1} round !!!")
            player_score += 1
            computer_score += 1
            num -= 1
            continue

        super_heroes = battle_result[player]

        found = False
        message = ''

        for hero in super_heroes:
            if computer in  hero:
                found = True
                message = hero[computer]
                break

        if found == True:
            print(message)
            player_score += 1
            print(f"player won {total_round - num + 1} round")

        else:
            print(f"computer won {total_round - num + 1} round")
            computer_score += 1

        num -= 1

        print()
#Printing the score each particiant have.
    print(f"Player Score :  {player_score}")
    print(f"Computer Score : {computer_score}")
#Do you want to play again????
    choice = input("Do you want to play again : Y/N ").lower()
    if choice in {"y","Y"}:
        num = int(input("Please enter the number of rounds: "))
        if(num%2==0):
            num += 1

        player_score = 0
        computer_score = 0

        total_round = num

        playAgain = True

    else:
        print("See you next time chicken !!!")
        break




        
                
