"""
🔢 The Magical Number Multiplier 🪄
================================
Watch as your number grows through
mystical mathematical powers!
================================
"""

import time
import os
from typing import Union

# Magical constants
THRESHOLD = 100
ANIMATION_CHARS = "⚡✨💫⭐"

def clear_screen() -> None:
    """Clears console for magical effects"""
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_multiplication(value: Union[int, float]) -> None:
    """Creates a magical multiplication animation"""
    for char in ANIMATION_CHARS:
        clear_screen()
        print(f"\n{char} Transforming {value}...")
        time.sleep(0.2)

def display_number_state(value: Union[int, float], step: int) -> None:
    """Shows the current state of the magical number"""
    # Create progress bar based on proximity to threshold
    progress = min(int((value / THRESHOLD) * 10), 10)
    bar = "🌟" * progress + "⭐" * (10 - progress)
    
    print(f"\n[Step {step}] Power Level: [{bar}]")
    print(f"📊 Current Value: {value:,.2f}")
    
    # Add dramatic messages based on value
    if value < 50:
        print("🌱 The number is growing steadily...")
    elif value < 75:
        print("🌿 The magic is intensifying!")
    else:
        print("🌳 Almost at maximum power!")

def get_starting_number() -> float:
    """Gets the initial number from the user"""
    while True:
        try:
            print("🎯 Enter a number to begin the magical multiplication:")
            num = float(input(">> "))
            if num <= 0:
                print("⚠️ Please enter a positive number!")
                continue
            return num
        except ValueError:
            print("⚠️ That's not a valid number!")

def main():
    print("✨ Welcome to the Magical Number Multiplier! ✨")
    print("Where numbers grow beyond imagination...\n")
    
    curr_value = get_starting_number()
    original_value = curr_value
    step = 0
    
    print("\n🪄 Let the multiplication begin!")
    print("=" * 50)
    
    while curr_value < THRESHOLD:
        step += 1
        animate_multiplication(curr_value)
        curr_value *= 2
        display_number_state(curr_value, step)
        time.sleep(1)
    
    print("\n🎉 The magic has reached its peak!")
    print(f"Your number grew from {original_value:,.2f} to {curr_value:,.2f}")
    print(f"Through {step} magical transformations! ✨")

if __name__ == '__main__':
    main()