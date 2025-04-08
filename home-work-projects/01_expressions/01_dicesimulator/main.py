"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how to use functions and random numbers.
It also demonstrates the use of global variables.
"""

import random

NUM_SIDES = 6

def roll_dice():
    """Simulates rolling two dice and prints their total"""
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Total: {total}")

def main():
    die1 = 10
    print(f"die1 starts as: {die1}")
    
    print("\nRoll 1:")
    roll_dice()
    print("\nRoll 2:")
    roll_dice()
    print("\nRoll 3:")
    roll_dice()
    
    print(f"\ndie1 ends as: {die1}")

if __name__ == '__main__':
    main()