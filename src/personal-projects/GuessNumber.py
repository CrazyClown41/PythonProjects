# Program that has the user guess a number between 1 and 25 with one try and tells them if it is higher or lower
#TODO want to give user a fixed amount of tries to guess the same random number 

import random

def getNum():
    num = int(input("Guess a number from 1 - 25: "))
    if num <= 25 and num >= 1:
        return num
    else:
        print("The number you entered is not between 1 and 25.")

def randomNum():
    randomNum = random.randint(1, 25)
    return randomNum

def guess(randomNum, num):
    if num == randomNum:
        print("You guessed the right number!")
    elif num < randomNum:
        print("Your number is too low. Guess again!")
    elif num > randomNum:
        print("Your number is too high. Guess again!")

guess(randomNum(),getNum())