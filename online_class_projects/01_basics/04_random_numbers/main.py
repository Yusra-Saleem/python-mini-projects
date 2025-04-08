"""
🎲 The Mystical Number Generator 🎲
================================
Watch as the cosmos reveals its
numerical secrets!
================================
"""

import random
import time
from typing import List

# Magical constants
N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def generate_mystical_number() -> int:
    """Channels the cosmic forces to generate a number"""
    return random.randint(MIN_VALUE, MAX_VALUE)

def display_number(number: int, index: int) -> None:
    """Presents each number with mystical flair"""
    # Rotating symbols for variety
    symbols = ['✨', '🌟', '💫', '⭐', '🔮']
    symbol = symbols[index % len(symbols)]
    
    # Visual bar representing number magnitude
    magnitude = int((number / MAX_VALUE) * 10)
    power_bar = '█' * magnitude + '▒' * (10 - magnitude)
    
    # Number properties
    properties = []
    if number % 2 == 0:
        properties.append("Even")
    else:
        properties.append("Odd")
    if number % 5 == 0:
        properties.append("Quintessential")
    if number > 75:
        properties.append("Powerful")
    
    print(f"\n{symbol} Number {index + 1}: {number}")
    print(f"Power Level: [{power_bar}] {number}%")
    print(f"Properties: {', '.join(properties)}")
    time.sleep(0.5)  # Dramatic pause

def main():
    print("🎮 Welcome to the Mystical Number Generator! 🎮")
    print("Preparing to channel the cosmic forces...\n")
    time.sleep(1)
    
    print("🌟 Generating mystical sequence...")
    print("═" * 40)
    
    total_sum = 0
    numbers = []
    
    for i in range(N_NUMBERS):
        number = generate_mystical_number()
        numbers.append(number)
        total_sum += number
        display_number(number, i)
    
    print("\n✨ Mystical Statistics ✨")
    print("═" * 40)
    print(f"Average Value: {total_sum/N_NUMBERS:.1f}")
    print(f"Highest Number: {max(numbers)}")
    print(f"Lowest Number: {min(numbers)}")
    print("═" * 40)
    
    print("\n🎲 The cosmic forces have spoken!")

if __name__ == '__main__':
    main()