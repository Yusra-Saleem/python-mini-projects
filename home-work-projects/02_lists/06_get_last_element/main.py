"""
🎯 The Last Element Explorer 🎯
===========================
A magical journey to discover the final
treasure in your list! Let's find what
comes last...
===========================
"""

import time


def get_last_element(lst: list) -> None:
    """Reveals the last element of your magical list with style"""
    print("\n✨ *Magical detection in progress* ✨")
    time.sleep(0.5)  # Create suspense
    print(f"\n🌟 The final treasure is: '{lst[-1]}' 🌟")

def get_lst() -> list:
    """Collects elements for your magical list"""
    lst = []
    print("🎭 Enter your magical elements...")
    print("(Press Enter without text to finish)\n")
    
    while True:
        elem = input("✨ Add to your collection: ")
        if elem == "":
            break
        lst.append(elem)
        print(f"Current collection: [{', '.join(repr(item) for item in lst)}]")
    
    return lst

def display_list_stats(lst: list) -> None:
    """Shows your magical collection statistics"""
    print("\n📜 Your Magical Collection Stats")
    print("═" * 50)
    print(f"Total items: {len(lst)}")
    print(f"First item: '{lst[0]}'")
    print(f"Last item: '{lst[-1]}'")
    print("Full collection:")
    print(f"[{', '.join(repr(item) for item in lst)}]")
    print("═" * 50)

def main():
    import time  # For dramatic pauses
    
    print("🎮 Welcome to the Last Element Explorer! 🎮")
    print("Where we discover the final treasure in your list...\n")
    
    lst = get_lst()
    
    if not lst:
        print("\n⚠️ The magical collection cannot be empty! ⚠️")
        return
    
    display_list_stats(lst)
    get_last_element(lst)
    print("\n✨ Thank you for exploring your list's secrets! ✨")

if __name__ == '__main__':
    main()