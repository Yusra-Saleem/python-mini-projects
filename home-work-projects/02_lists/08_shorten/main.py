"""
✂️ The Magical List Shortener ✂️
================================
A mystical tool that transforms long lists 
into elegant, concise collections!
================================
"""

import time
import random

MAX_LENGTH = 3
MYSTICAL_COLORS = ['🔵', '🟣', '🟡', '⚪', '🔴']

def display_list(lst: list, title: str) -> None:
    """Displays the magical list with animated borders"""
    print(f"\n{title}")
    border = "•*•" * 15
    print(border)
    print(f"[{' → '.join(f'{random.choice(MYSTICAL_COLORS)} {item}' for item in lst)}]")
    print(f"✨ Collection size: {len(lst)} items")
    print(border)

def shorten(lst: list) -> None:
    """Magically shortens the list with dramatic effect"""
    if len(lst) <= MAX_LENGTH:
        print(f"\n✨ Your collection is already perfectly balanced! ({len(lst)} items)")
        return

    print("\n🎭 Beginning the magical reduction ceremony...")
    time.sleep(1)
    
    print("\nRemoved treasures:")
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(f"✂️ '{removed_item}' vanishes in a puff of stardust! ✨")
        time.sleep(0.5)

def get_lst() -> list:
    """Collects items with magical flourish"""
    lst = []
    print("🎮 Enter your magical elements...")
    print(f"(The ancient scrolls decree a limit of {MAX_LENGTH} items)\n")
    
    item_count = 1
    while True:
        elem = input(f"🌟 Treasure #{item_count}: ")
        if not elem:
            if not lst:
                print("⚠️ The magical void cannot be empty! Try again...")
                continue
            break
            
        lst.append(elem)
        print(f"\n✨ Current collection:")
        display_list(lst, "📜 Magical Registry")
        item_count += 1
    
    return lst

def main():
    print("🌟 Welcome to the Ancient List Shortener! 🌟")
    print("Where lengthy collections transform into elegant essence...\n")
    
    lst = get_lst()
    
    print("\n🎭 Examining your magical collection...")
    time.sleep(1)
    
    display_list(lst, "📝 Your Original Treasures")
    shorten(lst)
    
    print("\n✨ The transformation is complete!")
    display_list(lst, "🎉 Your Refined Collection")
    
    print("\n🌟 Thank you for participating in this magical ceremony! 🌟")
    print("May your lists forever remain elegantly concise...")

if __name__ == '__main__':
    main()