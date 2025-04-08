"""
🚀 Mission Control: Launch Sequence 🚀
===================================
Initiating countdown for the most
epic space journey ever!
===================================
"""

import time
import os
from typing import List

# Mission constants
COUNTDOWN_START = 10
SYSTEMS = {
    10: "📡 Communication systems online",
    8: "⚡ Power systems nominal",
    6: "🛰️ Navigation systems ready",
    4: "🔥 Engine pre-ignition sequence",
    2: "💫 Launch stabilizers engaged"
}

def clear_screen() -> None:
    """Clears console for dramatic effect"""
    os.system('cls')

def display_rocket_animation(count: int) -> None:
    """Shows rocket animation based on countdown stage"""
    stages = [
        "  🚀\n  |\n  |\n ===",  # Normal
        "  🚀\n 💨|\n  |\n ===",  # Stage 1
        " 🚀\n 💨|\n 💨|\n ===",  # Stage 2
        "🚀\n💨|\n💨|\n===",      # Launch
    ]
    
    stage = max(0, min(3, (COUNTDOWN_START - count) // 3))
    print("\n" * 2)
    print(stages[stage])
    print("\n" * 2)

def display_countdown(count: int) -> None:
    """Shows countdown with system status"""
    # System status messages
    if count in SYSTEMS:
        print(f"\n{SYSTEMS[count]}")
    
    # Countdown display
    color = "🔴" if count <= 3 else "🟡" if count <= 7 else "🟢"
    print(f"\n{color} T-minus {count}")

def main():
    print("🌎 Welcome to Mission Control! 🌎")
    print("Initiating launch sequence...\n")
    time.sleep(2)
    
    for i in range(COUNTDOWN_START, 0, -1):
        clear_screen()
        display_rocket_animation(i)
        display_countdown(i)
        
        # Dramatic timing near launch
        delay = 1.5 if i <= 3 else 1.0
        time.sleep(delay)
    
    # Launch sequence
    clear_screen()
    print("\n" * 3)
    print("🚀 LIFTOFF! 🚀")
    print("We have cleared the tower!")
    print("\n🌠 Godspeed, brave astronauts!")

if __name__ == '__main__':
    main()