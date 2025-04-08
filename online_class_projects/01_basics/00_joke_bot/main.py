"""
🤣 The Ultimate Programming Joke Bot 3000 🤖
=========================================
Warning: Side effects may include uncontrollable 
laughter and coding inspiration!
=========================================
"""

import time
import random

JOKES = [
    {
        "setup": "Why do programmers prefer dark mode? 🌙",
        "punchline": "Because light attracts bugs! 🪲"
    },
    {
        "setup": "Why did the programmer quit his job? 💼",
        "punchline": "Because he didn't get arrays! 📊"
    },
    {
        "setup": "What did the Java Code say to the C code? ☕",
        "punchline": "You've got no class! 😎"
    },
    {
        "setup": "Why do programmers always mix up Halloween and Christmas? 🎃",
        "punchline": "Because Oct 31 = Dec 25! 🎄"
    },
    {
        "setup": "What's a programmer's favorite place in the house? 🏠",
        "punchline": "The Arrays Kitchen! 🍳"
    },
    {
        "setup": "Why was the math book sad? 📚",
        "punchline": "Because it had too many problems! 😢"
    },
    {
        "setup": "What did the proud router say to its child? 🌐",
        "punchline": "I byte because I love you! ❤️"
    }
]

SORRY_MESSAGES = [
    "🤖 ERROR 404: Humor in other topics not found!",
    "🎭 I only speak fluent joke-script!",
    "🤔 Does not compute... but I know some hilarious jokes!",
    "💫 My comedy processor only runs joke.exe",
    "🎪 I majored in Comedy at Robot University!"
]

def tell_random_joke() -> None:
    """Delivers a joke with perfect comedic timing"""
    joke = random.choice(JOKES)
    
    print("\n🎯 Loading comedy protocols...")
    time.sleep(1)
    
    print(f"\n{joke['setup']}")
    time.sleep(2)  # Perfect comedic pause
    
    print(f"{joke['punchline']}")
    time.sleep(1)
    
    print("\n*Robot laugh sounds* 🤖 HAHA-HA-HA-HA!")
    
def display_with_typing_effect(text: str) -> None:
    """Shows text with cool typing animation"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

# ...existing code for main() and other functions...