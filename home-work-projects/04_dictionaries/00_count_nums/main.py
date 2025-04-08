"""
🔮 The Mystical Number Counter 🔮
==============================
Where numbers reveal their secrets
and patterns emerge from chaos!
==============================
"""

import time
from typing import Dict, List

def get_user_numbers() -> List[int]:
    """Collects mystical numbers from the user"""
    numbers = []
    print("✨ Share your mystical numbers...")
    print("(Press Enter without a number to complete the ritual)\n")
    
    while True:
        try:
            user_input = input("🎲 Speak a number into the void: ")
            if not user_input:
                if not numbers:
                    print("⚠️ The void requires at least one number!")
                    continue
                break
                
            num = int(user_input)
            numbers.append(num)
            print(f"✨ {num} has been added to the collection...")
            
        except ValueError:
            print("⚠️ Only pure numbers hold magical properties!")
    
    return numbers

def count_nums(numbers: List[int]) -> Dict[int, int]:
    """Analyzes the frequency of mystical numbers"""
    print("\n🌟 The ancient counting ritual begins...")
    time.sleep(1)
    
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
        
    return frequency

def print_counts(frequency: Dict[int, int]) -> None:
    """Reveals the mystical patterns"""
    print("\n📜 The Sacred Scroll of Numbers reveals:")
    print("═" * 40)
    
    for num, count in sorted(frequency.items()):
        symbol = "⭐" if count > 1 else "✨"
        times = "time" if count == 1 else "times"
        print(f"{symbol} The number {num} appears {count} {times}")
    
    print("═" * 40)
    
    most_common = max(frequency.items(), key=lambda x: x[1])
    print(f"\n🏆 The most powerful number is {most_common[0]},")
    print(f"   appearing {most_common[1]} times in the sequence!")

def main():
    print("🎭 Welcome to the Mystical Number Counter! 🎭")
    print("Where we unveil the secrets of numerical patterns...\n")
    
    numbers = get_user_numbers()
    frequency = count_nums(numbers)
    print_counts(frequency)
    
    print("\n✨ The ritual is complete! May your numbers bring you fortune! ✨")

if __name__ == '__main__':
    main()