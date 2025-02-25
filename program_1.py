#Timothy Foster, 2/24/25, Random Dice Program

#Import the random module.
import random

#Define the variables that will later be used.
diceSum = 0
diceTotal = 0

#Create the function.
def randDice():

    #Assign two random integers to the variables.
    number_1 = random.randint(1,6)
    number_2 = random.randint(1,6)

    #Calculate the sum.
    diceSum = number_1 + number_2

    #Return the value of the sum.
    return diceSum

#Start the for loop.
for y in range(1, 100):

    #Keep track of the dice total by adding each iteration's sum.
    diceTotal = diceTotal + randDice()

#Calculate and round the average.
diceAverage = round(diceTotal/100, 2)

#Print the results.
print(f"The average of the 100 dice rolls was {diceAverage}.")
