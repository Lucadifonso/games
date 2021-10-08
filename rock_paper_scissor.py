'''
Make a two-player Rock-Paper-Scissors game.
Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner.
Ask if the players want to start a new game)

'''

# RULES
'''
Rock beats scissors
Scissors beats paper
Paper beats rock
'''


# Ask players

Name1 = input("What is your name Player1?")
print()
Name2 = input("What is your name Player2?")
print()
print("Ok " + Name1 + " and " + Name2 + " time to see who is the best one!")
print()
Hand1 = input("Hello " + Name1 + " chose 'rock','scissor' or 'paper'").lower()
Hand2 = input("Hello " + Name2 + " chose 'rock','scissor' or 'paper'").lower()
 

# Compare two hands

while Hand1 == "rock":      # Hand1 ROCK
    if Hand2 == "rock":
        print("None of you won! DRAW!")
        print()
        tryagain = input("Do you wanna try again? Type 'yes' or 'no'")
        if tryagain == "yes":
            Hand1 = input("Hello " + Name1 + " chose 'rock','scissor' or 'paper'")
            print()
            Hand2 = input("Hello " + Name2 + " chose 'rock','scissor' or 'paper'")
        if tryagain == "no":
            print("Hope you had fun")
            break

    if Hand2 == "scissor":
        print(Name1 ," you won!")
        print()
        tryagain = input("Do you wanna try again? Type 'yes' or 'no'")
        if tryagain == "yes":
            Hand1 = input("Hello " + Name1 + " chose 'rock','scissor' or 'paper'")
            print()
            Hand2 = input("Hello " + Name2 + " chose 'rock','scissor' or 'paper'")
        if tryagain == "no":
            print("Hope you had fun")
            break
        
        
    if Hand2 == "paper":
        print(Name2, " you won!")
        print()
        tryagain = input("Do you wanna try again? Type 'yes' or 'no'")
        if tryagain == "yes":
            Hand1 = input("Hello " + Name1 + " chose 'rock','scissor' or 'paper'")
            print()
            Hand2 = input("Hello " + Name2 + " chose 'rock','scissor' or 'paper'")
        if tryagain == "no":
            print("Hope you had fun")
            break
        


while Hand1 == "scissor":      # Hand1 SCISSOR
    if Hand2 == "rock":
        print(Name2 ,"you won!")
        print()
        tryagain = input("Do you wanna try again? Type 'yes' or 'no'")
        if tryagain == "yes":
            Hand1 = input("Hello " + Name1 + " chose 'rock','scissor' or 'paper'")
            print()
            Hand2 = input("Hello " + Name2 + " chose 'rock','scissor' or 'paper'")
        if tryagain == "no":
            print("Hope you had fun")
            break
        

    if Hand2 == "scissor":
        print("None of you won! DRAW!")
        print()
        tryagain = input("Do you wanna try again? Type 'yes' or 'no'")
        if tryagain == "yes":
            Hand1 = input("Hello " + Name1 + " chose 'rock','scissor' or 'paper'")
            print()
            Hand2 = input("Hello " + Name2 + " chose 'rock','scissor' or 'paper'")
        if tryagain == "no":
            print("Hope you had fun")
            break
        
        
    if Hand2 == "paper":
        print(Name1 ,"you won!")
        print()
        tryagain = input("Do you wanna try again? Type 'yes' or 'no'")
        if tryagain == "yes":
            Hand1 = input("Hello " + Name1 + " chose 'rock','scissor' or 'paper'")
            print()
            Hand2 = input("Hello " + Name2 + " chose 'rock','scissor' or 'paper'")
        if tryagain == "no":
            print("Hope you had fun")
            break
        


while Hand1 == "paper":      # Hand1 PAPER
    if Hand2 == "rock":
        print(Name1 ," you won!")
        print()
        tryagain = input("Do you wanna try again? Type 'yes' or 'no'")
        if tryagain == "yes":
            Hand1 = input("Hello " + Name1 + " chose 'rock','scissor' or 'paper'")
            print()
            Hand2 = input("Hello " + Name2 + " chose 'rock','scissor' or 'paper'")
        if tryagain == "no":
            print("Hope you had fun")
            break
        

    if Hand2 == "paper":
        print("None of you won! DRAW!")
        print()
        tryagain = input("Do you wanna try again? Type 'yes' or 'no'")
        if tryagain == "yes":
            Hand1 = input("Hello " + Name1 + " chose 'rock','scissor' or 'paper'")
            print()
            Hand2 = input("Hello " + Name2 + " chose 'rock','scissor' or 'paper'")
        if tryagain == "no":
            print("Hope you had fun")
            break
        
        
    if Hand2 == "scissor":
        print(Name2 ,"you won!")
        print()
        tryagain = input("Do you wanna try again? Type 'yes' or 'no'")
        if tryagain == "yes":
            Hand1 = input("Hello " + Name1 + " chose 'rock','scissor' or 'paper'")
            print()
            Hand2 = input("Hello " + Name2 + " chose 'rock','scissor' or 'paper'")
        if tryagain == "no":
            print("Hope you had fun")
            break
        
    



