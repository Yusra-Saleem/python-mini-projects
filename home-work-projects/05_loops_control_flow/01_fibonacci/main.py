"""
🌀 The Fibonacci Spiral Explorer 🌀
================================
Discover nature's mathematical poetry,
from rabbit populations to spiral galaxies!
================================
"""

import time
from typing import Generator, Tuple
from math import log

# Magical constants
MAX_TERM_VALUE = 10000
GOLDEN_RATIO = 1.618034

def generate_fibonacci() -> Generator[Tuple[int, int, int], None, None]:
    """Generates Fibonacci numbers with position and golden ratio accuracy"""
    current, next_term = 0, 1
    position = 0
    
    while current <= MAX_TERM_VALUE:
        golden_accuracy = 0
        if position > 1:
            ratio = next_term / current
            golden_accuracy = 100 - abs(ratio - GOLDEN_RATIO) * 100
        yield position, current, golden_accuracy
        current, next_term = next_term, current + next_term
        position += 1

def display_number(position: int, number: int, golden_accuracy: float) -> None:
    """Displays each Fibonacci number with artistic flair"""
    # Visual elements for different number ranges
    if number == 0:
        prefix = "🌱"  # Seed
    elif number < 10:
        prefix = "🌿"  # Sprout
    elif number < 100:
        prefix = "🌸"  # Flower
    elif number < 1000:
        prefix = "🌳"  # Tree
    else:
        prefix = "🌟"  # Star

    # Create visual growth bar
    length = min(10, int(log(number + 1, 2)))
    growth_bar = "▰" * length + "▱" * (10 - length)
    
    # Show golden ratio accuracy for numbers after first two
    ratio_info = ""
    if position > 1:
        stars = int(golden_accuracy / 20)
        ratio_info = f"[φ: {'★' * stars}{'☆' * (5 - stars)}]"
    
    print(f"{prefix} Fib({position:2d}) = {number:6d} {growth_bar} {ratio_info}")
    time.sleep(0.3)

def main():
    print("✨ Welcome to the Fibonacci Spiral Explorer! ✨")
    print("Watch as nature's sequence unfolds before you...\n")
    
    print("📊 Sequence Growth Pattern:")
    print("═" * 60)
    
    for position, number, golden_accuracy in generate_fibonacci():
        display_number(position, number, golden_accuracy)
    
    print("═" * 60)
    print("\n🎭 The sequence has revealed its pattern!")
    print("Each number is a window into nature's divine proportion...")

if __name__ == '__main__':
    main()