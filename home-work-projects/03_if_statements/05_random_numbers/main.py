"""
🎲 The Mystical Number Oracle 🎲
============================
Where random becomes magical and
numbers tell their own tales!
============================
"""

import random
import time

# Magical constants
N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

# Mystical decorations
SYMBOLS = ['✨', '🌟', '🔮', '⭐', '💫']
COLORS = ['royal', 'mystical', 'enchanted', 'celestial', 'magical']

def generate_mystical_number() -> int:
    """Summons a mystical number from the ethereal realm"""
    return random.randint(MIN_VALUE, MAX_VALUE)

def display_prophecy(number: int, index: int) -> None:
    """Reveals a mystical number with magical flourish"""
    symbol = SYMBOLS[index % len(SYMBOLS)]
    color = COLORS[index % len(COLORS)]
    print(f"{symbol} The {color} number reveals itself: {number}")
    time.sleep(0.5)  # Dramatic pause

def main():
    print("🎭 Welcome to the Mystical Number Oracle! 🎭")
    print("Prepare to witness the revelation of 10 sacred numbers...")
    print("\n✨ Let the divination begin! ✨\n")
    
    for i in range(N_NUMBERS):
        mystical_number = generate_mystical_number()
        display_prophecy(mystical_number, i)
    
    print("\n🌟 The prophecy is complete! 🌟")
    print("May these numbers bring you fortune and wisdom...")

if __name__ == '__main__':
    main()