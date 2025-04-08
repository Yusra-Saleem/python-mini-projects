"""
🔄 The Magical List Multiplier 🔄
===============================
Watch as your message gets magically replicated!
Witness the power of mutable data structures...
===============================
"""

def add_three_copies(magic_list: list, message: str) -> None:
    """Creates three magical copies of your message in the list"""
    print("\n✨ *Magical multiplication in progress* ✨")
    for i in range(3):
        magic_list.append(message)
        print(f"Copy {i+1} created: {magic_list}")
        time.sleep(0.5)  # Add dramatic pause

def display_list_state(title: str, items: list) -> None:
    """Displays the current state of our magical list"""
    print(f"\n{title}")
    print("═" * 40)
    if not items:
        print("[ Empty magical container ]")
    else:
        print(f"[{', '.join(repr(item) for item in items)}]")
    print("═" * 40)

def main():
    print("🎭 Welcome to the Magical List Multiplier! 🎭")
    print("Where one message becomes many...\n")
    
    message = input("✍️ Enter your magical message: ")
    magical_list = []
    
    display_list_state("📝 Your Magical Container (Before)", magical_list)
    add_three_copies(magical_list, message)
    display_list_state("🎉 Your Magical Container (After)", magical_list)
    
    print("\n🌟 The magic of mutable data structures! 🌟")

if __name__ == "__main__":
    import time  # For dramatic pauses
    main()