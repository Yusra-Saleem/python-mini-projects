"""
📞 The Enchanted Communication Codex 📞
===================================
Where names and numbers weave together
in magical connections!
===================================
"""

import time
from typing import Dict, Optional

def add_contact(phonebook: Dict[str, str], name: str, number: str) -> None:
    """Records a new magical connection"""
    phonebook[name] = number
    print(f"✨ {name}'s magical frequency has been recorded!")
    time.sleep(0.5)

def read_phone_numbers() -> Dict[str, str]:
    """Creates new entries in the magical codex"""
    phonebook = {}
    print("📚 Welcome to the Enchanted Contact Registry!")
    print("(Press Enter without a name to complete your entries)\n")
    
    while True:
        name = input("🔮 Speak the name of your contact: ").strip()
        if not name:
            break
            
        number = input("📱 Share their mystical number: ").strip()
        if not number:
            print("⚠️ A contact must have a number!")
            continue
            
        add_contact(phonebook, name, number)
    return phonebook

def display_contacts(phonebook: Dict[str, str]) -> None:
    """Reveals all magical connections"""
    if not phonebook:
        print("\n📖 The codex appears to be empty...")
        return
        
    print("\n📖 The Mystical Directory reveals:")
    print("═" * 40)
    for name, number in sorted(phonebook.items()):
        print(f"✨ {name} ←→ {number}")
    print("═" * 40)

def main():
    print("🎭 Welcome to the Enchanted Communication Codex! 🎭")
    print("Where every number holds a magical connection...\n")
    
    phonebook = read_phone_numbers()
    
    if phonebook:
        display_contacts(phonebook)
    
    print("\n✨ Thank you for using the Enchanted Codex! ✨")
    print("May your communications be blessed with magic!")

if __name__ == '__main__':
    main()