"""
✨ The Positivity Enchanter ✨
==========================
Where affirmations become magical
spells of self-empowerment!
==========================
"""

import time
import random
from typing import List

# Magical constants
AFFIRMATION = "I am capable of doing anything I put my mind to."
ENCOURAGEMENTS = [
    "You're getting closer! Keep the positive energy flowing! ⭐",
    "That's the spirit! Almost there! 🌟",
    "Feel the power of positive thinking! Try again! 💫",
    "You've got this! Let's try once more! ✨"
]

def display_magical_text(text: str, delay: float = 0.03) -> None:
    """Displays text with a magical typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def calculate_similarity(attempt: str, target: str) -> float:
    """Calculates how close the attempt is to the target"""
    matches = sum(1 for a, b in zip(attempt, target) if a == b)
    return matches / max(len(attempt), len(target)) * 100

def display_progress(similarity: float) -> None:
    """Shows magical progress bar"""
    progress = int(similarity / 10)
    bar = '✨' * progress + '⭐' * (10 - progress)
    print(f"\nProgress: [{bar}] {similarity:.1f}%")

def main():
    display_magical_text("\n🌟 Welcome to the Positivity Enchanter! 🌟")
    time.sleep(0.5)
    
    print("\nChannel your inner strength by reciting this powerful affirmation:")
    display_magical_text(f"✨ {AFFIRMATION} ✨\n")
    
    attempt_count = 0
    while True:
        attempt_count += 1
        user_input = input("Your magical words: ").strip()
        
        if user_input == AFFIRMATION:
            print("\n🎉 MAGNIFICENT! 🎉")
            display_magical_text("You've unlocked the power within!")
            print(f"\n💫 It took {attempt_count} attempts to align your energy perfectly!")
            break
        
        similarity = calculate_similarity(user_input, AFFIRMATION)
        display_progress(similarity)
        print(random.choice(ENCOURAGEMENTS))
        print("\nLet's try that affirmation again:")
        display_magical_text(f"✨ {AFFIRMATION} ✨\n")

if __name__ == '__main__':
    main()