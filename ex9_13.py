#!/usr/bin/env python3
"""
 Make a class Die with one attribute called sides which has a default value of 6. 
 Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.
 make a 6 sided die and roll it 10 times
"""
from random import randint

class Die:
    "A simple Die from books exercise"
    def __init__(self, sides=6):
        self.sides=sides

    def roll_die(self):
        return randint(1,self.sides)



def roll_10_times():
    my_die = Die()

    for i in range(10):
       print(my_die.roll_die())

"""
 Create a 10 sided die and a 20 sided die
 roll each die 10 times.
"""
def roll_d10_and_d20():
    d10 = Die(10)
    d20 = Die(20)

    for i in range(10):
        print(f"{i+1}: d10 = {d10.roll_die()} d20 = {d20.roll_die()}")

if __name__ == "__main__":
    roll_10_times()
    print('-'*20)
    roll_d10_and_d20()


