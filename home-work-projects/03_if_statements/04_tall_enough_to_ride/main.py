"""
🎢 The Enchanted Rollercoaster Gateway 🎢
=====================================
Where magic meets adventure, and height
determines your destiny!
=====================================
"""

import time

# Magical constants
MINIMUM_HEIGHT = 50  # mystical units
RIDES = {
    "Dragon's Flight": {"min_height": 50, "symbol": "🐉"},
    "Unicorn Carousel": {"min_height": 30, "symbol": "🦄"},
    "Wizard's Tower Drop": {"min_height": 60, "symbol": "🧙‍♂️"}
}

def check_height_requirements(height: float) -> None:
    """Determines eligibility for magical rides"""
    print("\n✨ Consulting the magical measuring crystal...")
    time.sleep(1)
    
    eligible_rides = []
    future_rides = []
    
    for ride, info in RIDES.items():
        if height >= info["min_height"]:
            eligible_rides.append(f"{info['symbol']} {ride}")
        else:
            future_rides.append(f"{info['symbol']} {ride}")
    
    if eligible_rides:
        print("\n🎉 Wonderful news, brave adventurer!")
        print("You're ready to experience these magical rides:")
        for ride in eligible_rides:
            print(f"  ✨ {ride}")
    
    if future_rides:
        print("\n🌟 Future adventures await:")
        for ride in future_rides:
            print(f"  ⏳ {ride} - Keep growing!")

def main():
    print("🎪 Welcome to the Mystical Amusement Park! 🎪")
    print("Where dreams take flight and adventures await...\n")
    
    while True:
        try:
            height_input = input("🔮 Reveal your height (or press Enter to exit): ")
            
            if not height_input:
                print("\n✨ Thank you for visiting the Mystical Park! ✨")
                break
                
            height = float(height_input)
            
            if height <= 0:
                print("⚠️ Even pixies aren't that small!")
                continue
            if height > 300:
                print("⚠️ Even giants aren't that tall!")
                continue
                
            check_height_requirements(height)
            
        except ValueError:
            print("⚠️ That's not a magical measurement!")

if __name__ == '__main__':
    main()