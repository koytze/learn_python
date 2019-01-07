"""A mini dice guessing game.
Player choose a number, not bigger than the max possible value
and computer will choose 2 random numbers and will compare their
with number chosen by player"""

""" The program does the following:

    Roll a pair of dice.
    Add the values of the roll.
    Ask the user to guess a number.
    Compare the user's guess to the total value.
    Determine the winner (user or computer).

"""
from random import randint
from time import sleep

"Let the user to choos the number of sides a dice can have"
number_of_sides = int(input("How many sides a dice should have? [1-6] "))

def get_user_guess():
  guess = int(input("Guess a number: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1,number_of_sides)
  second_roll = randint(1,number_of_sides)
  max_val = number_of_sides * 2
  print("Max value is: %02d" % (max_val))
  guess = get_user_guess()
  
  if guess > max_val:
    print("Your guess value is bigger than maximum possible number!")
  else:
    print("Rolling...")
    sleep(2)
    print("First dice roll: %02d" % (first_roll))
    sleep(1)
    print("Second dice roll: %02d" % (second_roll))
    sleep(1)
    total_roll = first_roll + second_roll
    print("Result... %02d" % (total_roll))
    sleep(1)
    
    if guess == total_roll:
      print("It looks like you lucky guess it! Your guess, %02d matches the sum of rolling dice: %02d! Congrats!" % (guess,total_roll))
    else:
      print("Alas! You've lost this time! Your guess: %02d, did not match the sum of rolling dice: %02d! Ready for a second round?" % (guess,total_roll))

roll_dice(number_of_sides)
