"""
🗳️ The Global Voting Adventure! 🌍
================================
Discover your voting rights across
magical lands and distant realms!
================================
"""

import time

# Magical Voting Kingdoms and their ancient laws
COUNTRIES = {
    "Peturksbouipo": {"age": 16, "symbol": "🌟", "title": "Land of Young Voices"},
    "Stanlau": {"age": 25, "symbol": "🌙", "title": "Realm of Wise Decisions"},
    "Mayengua": {"age": 48, "symbol": "👑", "title": "Empire of Elder Wisdom"}
}

def check_voting_rights(age: int) -> None:
    """Reveals voting rights with magical flourish"""
    print("\n✨ Consulting the ancient voting scrolls...")
    time.sleep(1)
    
    for country, info in COUNTRIES.items():
        print(f"\n{info['symbol']} {country} - {info['title']}")
        print("." * 40)
        
        if age >= info['age']:
            print(f"🎉 Rejoice! You can vote in {country},")
        else:
            years_left = info['age'] - age
            print(f"⏳ Alas! You cannot yet vote in {country},")
        
        print(f"   where the sacred voting age is {info['age']}")
        time.sleep(0.5)

def main():
    print("🌟 Welcome to the Mystical Voting Rights Explorer! 🌟")
    print("Discover your voting destiny across three magical lands...\n")
    
    try:
        age = int(input("🎭 Reveal your age, young traveler: "))
        if age < 0:
            print("\n⚠️ Time travelers from the past cannot vote!")
            return
        if age > 150:
            print("\n⚠️ Even the most ancient wizards aren't that old!")
            return
            
        check_voting_rights(age)
        
        print("\n📜 The prophecy is complete!")
        if age < 16:
            print("Keep growing, young one. Your time will come!")
        elif age < 25:
            print("You've begun your voting journey!")
        elif age < 48:
            print("Your voice grows stronger with time!")
        else:
            print("You've achieved full voting wisdom!")
            
    except ValueError:
        print("\n⚠️ That's not a valid age in any realm!")

if __name__ == '__main__':
    main()