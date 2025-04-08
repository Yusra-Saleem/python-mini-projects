"""
🎮 The Mystical Number Quest 🔮
===========================
A magical journey to discover the
hidden number in the void!
===========================
"""

import random
import time
from typing import Tuple

def get_difficulty() -> Tuple[int, int, int]:
    """Sets the game difficulty and returns range and attempts"""
    print("\n👑 Choose your challenge level:")
    print("1. Apprentice (1-50, 10 attempts)")
    print("2. Mage (1-100, 7 attempts)")
    print("3. Archmage (1-200, 5 attempts)")
    
    while True:
        try:
            level = int(input("\n🎯 Select your destiny (1-3): "))
            if level == 1:
                return (1, 50, 10)
            elif level == 2:
                return (1, 100, 7)
            elif level == 3:
                return (1, 200, 5)
            print("⚠️ Please choose 1, 2, or 3!")
        except ValueError:
            print("⚠️ That's not a valid choice!")

def display_guess_feedback(guess: int, secret: int, attempts: int, max_attempts: int) -> None:
    """Provides magical feedback on the guess"""
    # Create energy bar
    energy = "⚡" * attempts + "💨" * (max_attempts - attempts)
    print(f"\nMagical energy remaining: [{energy}]")
    
    # Calculate how close the guess was
    difference = abs(secret - guess)
    if difference > 50:
        hint = "You're lost in the void!"
    elif difference > 20:
        hint = "The magic is faint..."
    elif difference > 10:
        hint = "You're getting warmer!"
    else:
        hint = "The magic is very strong!"
    
    # Show hint with arrow indicating direction
    print(f"{'🔥' if guess < secret else '❄️'} {hint}")

def main():
    print("🎮 Welcome to the Mystical Number Quest! 🎮")
    print("Where numbers hide in magical realms...")
    
    min_num, max_num, max_attempts = get_difficulty()
    secret_number = random.randint(min_num, max_num)
    attempts_left = max_attempts
    guesses = []
    
    print(f"\n🔮 I am thinking of a number between {min_num} and {max_num}...")
    time.sleep(1)
    
    while attempts_left > 0:
        try:
            guess = int(input(f"\n✨ Enter your guess ({attempts_left} attempts left): "))
            
            if guess < min_num or guess > max_num:
                print(f"⚠️ Please guess between {min_num} and {max_num}!")
                continue
                
            if guess in guesses:
                print("🔄 You've already tried that number!")
                continue
                
            guesses.append(guess)
            attempts_left -= 1
            
            if guess == secret_number:
                print("\n🎉 CONGRATULATIONS! 🎉")
                print(f"✨ The mystical number was indeed: {secret_number}")
                print(f"🎯 You succeeded with {attempts_left} attempts remaining!")
                return
            
            display_guess_feedback(guess, secret_number, attempts_left, max_attempts)
            
        except ValueError:
            print("⚠️ That's not a valid number!")
    
    print("\n💔 Game Over! You've run out of magical energy!")
    print(f"🎲 The mystical number was: {secret_number}")

if __name__ == '__main__':
    main()