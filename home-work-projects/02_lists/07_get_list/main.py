"""
📝 The Magical List Builder 📝
==========================
Create your own magical collection
one element at a time!
==========================
"""

def display_list_status(lst: list) -> None:
    """Shows the current state of the magical collection"""
    print("\n🎭 Current Collection:")
    print("═" * 40)
    if not lst:
        print("[ Empty ]")
    else:
        print(f"[{', '.join(repr(item) for item in lst)}]")
    print("═" * 40)
    print(f"Items collected: {len(lst)}\n")

def get_magical_list() -> list:
    """Collects items for the magical list"""
    magical_list = []
    
    while True:
        display_list_status(magical_list)
        value = input("✨ Add to your collection (or press Enter to finish): ")
        
        if not value:
            break
            
        magical_list.append(value)
        print(f"🌟 '{value}' has been added to your collection!")

    return magical_list

def main():
    print("🎮 Welcome to the Magical List Builder! 🎮")
    print("Where your collection comes to life...\n")
    
    collection = get_magical_list()
    
    print("\n🎉 Your Final Magical Collection:")
    print("═" * 40)
    print(f"[{', '.join(repr(item) for item in collection)}]")
    print("═" * 40)
    print(f"\n✨ Total items collected: {len(collection)}")
    print("\nThank you for building your magical collection! 🌟")

if __name__ == '__main__':
    main()