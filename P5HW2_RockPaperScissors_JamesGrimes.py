# Rock paper scissors game on python
# November 6th 2018
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# James Grimes
#

import random
def computer():
    computernumber = random.randint(1,3)
    if computernumber == 1:
        computerock()
    elif computernumber == 2:
        computerpaper()
    else:
        computerscissors()


def computerock():
    playerchoice = input("Rock, Paper or Scissors against the computer? :")
    if playerchoice == "Rock":
        print ("It is a tie! The computer has selected rock against your rock.")
    if playerchoice == "Paper":
        print ("You win! The computer has selected rock against your paper.")
    if playerchoice == "Scissors":
        print ("You lose! The computer has selected rock against your scissor.")

def computerpaper():
    playerchoice = input("Rock, Paper, or Scissors against the computer? :")
    if playerchoice == "Rock":
        print ("You lose! The computer has selected paper against your rock.")
    if playerchoice == "Paper":
        print ("It is a tie! The computer has selected paper against your paper")
    if playerchoice == "Scissors":
        print ("You win! The computer has selected paper against your scissors")

def computerscissors():
    playerchoice = input("Rock, Paper, or Scissors against the computer? :")
    if playerchoice == "Rock":
        print ("You win! The computer has selected scissors against your rock.")
    if playerchoice == "Paper":
        print ("You lose! The computer has selected scissors against your paper")
    if playerchoice == "Scissors":
        print ("It is a tie! The computer has selected scissors against your scissors")
computer()

input("Press enter to close the program")

