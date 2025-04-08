"""
🔢 The Even Number Symphony 🎵
==========================
Where mathematics dances with
patterns of perfect balance!
==========================
"""

import time
from typing import Generator

def generate_even_numbers(count: int) -> Generator[int, None, None]:
    """Creates a stream of even numbers with mathematical grace"""
    for i in range(count):
        yield i * 2

def display_number(number: int, index: int) -> None:
    """Presents each even number with artistic flair"""
    symbols = ['🎵', '🎶', '🎼', '🎹']
    symbol = symbols[index % len(symbols)]
    
    # Create visual pattern bar
    pattern = '▮' * (number % 10 + 1)
    spacing = ' ' * (10 - len(pattern))
    
    print(f"{symbol} Even #{index+1:2d}: {number:2d} {spacing}{pattern}")
    time.sleep(0.2)  # Musical pause

def main():
    print("🎭 Welcome to the Even Number Symphony! 🎭")
    print("Where numbers create perfect harmony...\n")
    
    total_numbers = 20
    print("🎼 The Mathematical Melody Begins:")
    print("═" * 40)
    
    for index, number in enumerate(generate_even_numbers(total_numbers)):
        display_number(number, index)
    
    print("═" * 40)
    print("\n✨ The symphony is complete!")
    print(f"We've discovered {total_numbers} even numbers in perfect harmony.")

if __name__ == '__main__':
    main()