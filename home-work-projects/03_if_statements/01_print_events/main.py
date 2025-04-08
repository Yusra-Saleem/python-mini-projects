"""
🔢 The Even Number Adventure! 🔢
============================
Watch as we discover the magical
sequence of even numbers...
============================
"""

import time

def print_even_number(num: int, index: int) -> None:
    """Prints a single even number with style"""
    symbols = ['✨', '🌟', '💫', '⭐']
    symbol = symbols[index % len(symbols)]
    print(f"{symbol} Even number #{index + 1}: {num}")
    time.sleep(0.2)  # Add a slight delay for dramatic effect

def display_progress(current: int, total: int) -> None:
    """Shows progress through the number journey"""
    progress = int((current / total) * 20)
    bar = '🔵' * progress + '⚪' * (20 - progress)
    print(f"\rProgress: [{bar}] {current}/{total}", end='')

def main():
    print("🎮 Welcome to the Even Number Adventure! 🎮")
    print("Let's discover the first 20 even numbers...\n")
    
    total_numbers = 20
    
    print("🎯 Your magical sequence begins:\n")
    for i in range(total_numbers):
        even_num = i * 2
        print_even_number(even_num, i)
        display_progress(i + 1, total_numbers)
    
    print("\n\n✨ Adventure complete! ✨")
    print(f"We discovered {total_numbers} even numbers together!")

if __name__ == '__main__':
    main()