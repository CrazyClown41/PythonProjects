import random

def getInput():
    choice = str(input("Enter your choice (Rock, Paper, Scissors): "))
    if (choice == "Rock"):
        choice = 0
    elif (choice == "Paper"):
        choice = 1
    elif (choice == "Scissors"):
        choice = 2
    return choice

def randomNum(): 
    randomNum = random.randint(0, 2)
    return randomNum

def decision(choice, randomNum):
    if (choice == randomNum):
        print("It is a tie.")
    elif (choice == 0 and randomNum == 1):
        print("Computer Wins!")
    elif (choice == 1 and randomNum == 0):
        print("User Wins!")
    elif (choice == 0 and randomNum == 2):
        print("User Wins!")
    elif (choice == 2 and randomNum == 0):
        print("Computer Wins!")
    elif (choice == 1 and randomNum == 2):
        print("Computer Wins!")
    elif (choice == 2 and randomNum == 1):
        print("User Wins!")
    else:
        print("Something went wrong.")

decision(randomNum(),getInput())