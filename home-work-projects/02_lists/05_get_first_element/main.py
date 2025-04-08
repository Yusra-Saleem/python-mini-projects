"""
🎯 The First Element Finder 🎯
===========================
A magical journey to discover the leader
of your list! Let's find what comes first...
===========================
"""

def get_first_element(lst: list) -> None:
    """Reveals the first element of your magical list with style"""
    print("\n✨ *Magical detection in progress* ✨")
    print(f"\n🌟 The chosen one is: '{lst[0]}' 🌟")

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
        print(f"Current list: {lst}")
    
    return lst

def display_list(lst: list) -> None:
    """Shows your magical collection"""
    print("\n📜 Your Magical Collection")
    print("═" * 40)
    print(f"[{', '.join(repr(item) for item in lst)}]")
    print("═" * 40)

def main():
    print("🎮 Welcome to the First Element Finder! 🎮")
    print("Where we discover what leads your list...\n")
    
    lst = get_lst()
    
    if not lst:
        print("\n⚠️ The magical collection cannot be empty! ⚠️")
        return
    
    display_list(lst)
    get_first_element(lst)
    print("\n✨ Thank you for exploring your list's secrets! ✨")

if __name__ == '__main__':
    main()