"""
🚀 The Cosmic Launch Sequence 🚀
============================
Initiating countdown for an
epic journey to the stars!
============================
"""

import time
import os
from typing import List

# Mission constants
COUNTDOWN_START = 10
COUNTDOWN_DELAY = 1.0  # seconds between counts

def clear_screen() -> None:
    """Clears the console for dramatic effect"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_rocket_stage(count: int) -> None:
    """Displays rocket and launch pad animation"""
    stages = {
        10: "      🚀\n      |\n      |\n     ===",
        7:  "    💨🚀\n      |\n     ===",
        4:  "   💨💨🚀\n     ===",
        1:  "  💨💨💨🚀\n    ===",
        0:  "      🌠\n     ===\n    LIFTOFF!"
    }
    
    # Get closest stage or default to first stage
    stage = min([s for s in stages.keys() if s >= count], default=0)
    clear_screen()
    print("\n" * 2)
    print(stages[stage])
    print("\n" * 2)

def display_countdown(count: int) -> None:
    """Displays countdown with status indicators"""
    status = {
        10: "🔧 Systems Check",
        7: "⚡ Power Units Active",
        5: "💫 Navigation Online",
        3: "🔥 Engines Ignited",
        1: "✨ Launch Imminent"
    }
    
    # Show current status if available
    if count in status:
        print(f"\n{status[count]}")
    
    # Display countdown number with effects
    print(f"\n{'🔴' if count <= 3 else '🟡' if count <= 7 else '🟢'} T-{count}")

def main():
    print("🌎 Welcome to Mission Control! 🌎")
    print("Preparing for launch sequence...\n")
    time.sleep(2)
    
    for i in range(COUNTDOWN_START, -1, -1):
        display_rocket_stage(i)
        if i > 0:
            display_countdown(i)
        else:
            print("\n🚀 LIFTOFF! 🚀")
            print("We have achieved orbit!")
        
        # Add tension near launch
        delay = COUNTDOWN_DELAY * (2 if i <= 3 else 1)
        time.sleep(delay)

if __name__ == '__main__':
    main()