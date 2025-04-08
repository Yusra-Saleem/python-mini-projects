"""
🎲 The Mystical Number Quest 🎲
===========================
A magical journey to discover the
secret number hidden in the void!
===========================
"""

import random
import time
from typing import Tuple

def get_difficulty() -> Tuple[int, int, int]:
    """Let player choose their destiny"""
    print("\n👑 Choose your challenge level:")
    print("1. Apprentice (1-50, 10 attempts)")
    print("2. Mage (1-100, 8 attempts)")
    print("3. Archmage (1-200, 6 attempts)")
    
    while True:
        try:
            level = int(input("\n🎯 Enter your choice (1-3): "))
            if level == 1:
                return (1, 50, 10)
            elif level == 2:
                return (1, 100, 8)
            elif level == 3:
                return (1, 200, 6)
            else:
                print("⚠️ Please choose 1, 2, or 3!")
        except ValueError:
            print("⚠️ That's not a valid choice!")

def display_progress(attempts: int, max_attempts: int) -> None:
    """Shows magical energy remaining"""
    energy = "⚡" * attempts + "💨" * (max_attempts - attempts)
    print(f"\nMagical energy remaining: [{energy}] ({attempts}/{max_attempts})")

def main():
    print("🎮 Welcome to the Mystical Number Quest! 🎮")
    print("Where numbers hide in the shadows of magic...")
    
    min_num, max_num, max_attempts = get_difficulty()
    secret_number = random.randint(min_num, max_num)
    attempts = max_attempts
    guesses = []
    
    print(f"\n🔮 I am thinking of a number between {min_num} and {max_num}...")
    time.sleep(1)
    
    while attempts > 0:
        display_progress(attempts, max_attempts)
        
        try:
            guess = int(input("\n✨ Enter your guess: "))
            
            if guess < min_num or guess > max_num:
                print(f"⚠️ Please guess between {min_num} and {max_num}!")
                continue
                
            if guess in guesses:
                print("🔄 You've already tried that number!")
                continue
                
            guesses.append(guess)
            attempts -= 1
            
            if guess == secret_number:
                print("\n🎉 CONGRATULATIONS! 🎉")
                print(f"✨ The mystical number was indeed: {secret_number}")
                print(f"🎯 You solved it with {attempts} attempts remaining!")
                return
            
            # Provide more detailed feedback
            difference = abs(secret_number - guess)
            if difference > 50:
                hint = "You're lost in the void!"
            elif difference > 20:
                hint = "You're way off course!"
            elif difference > 10:
                hint = "Getting warmer..."
            else:
                hint = "You're very close!"
                
            print(f"\n{'🔥' if guess < secret_number else '❄️'} {hint}")
            
        except ValueError:
            print("⚠️ That's not a valid number!")
    
    print("\n💔 Game Over! You've run out of magical energy!")
    print(f"🎲 The mystical number was: {secret_number}")

if __name__ == '__main__':
    main()