"""
🎲 Lucky Dice Casino! 🎲
=======================
Roll the magical dice and test your luck!
Let fortune favor the bold...
=======================
"""

import random

NUM_SIDES = 6

def roll_dice() -> tuple[int, int]:
    return random.randint(1, NUM_SIDES), random.randint(1, NUM_SIDES)

def main():
    print("🎰 Welcome to the Lucky Dice Casino! 🎰")
    print("Where fortune meets fun...\n")
    
    die1, die2 = roll_dice()
    total = die1 + die2
    
    print("✨ The dice are rolling... ✨")
    print(f"\n🎲 First die shows: {die1}")
    print(f"🎲 Second die shows: {die2}")
    print(f"\n🌟 Grand total: {total} 🌟")
    
    if total == 12:
        print("\n🎉 JACKPOT! Perfect roll! 🎉")
    elif total == 2:
        print("\n🎭 Snake eyes! How mysterious... 🎭")
    else:
        print("\n🎪 Thanks for rolling with us! 🎪")

if __name__ == '__main__':
    main()