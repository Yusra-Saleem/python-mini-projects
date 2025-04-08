"""
🏪 The Enchanted Fruit Emporium 🍎
================================
Where magical fruits await your discovery
and your basket fills with wonder!
================================
"""

import time
from typing import Dict

# Magical fruit inventory with prices and special properties
FRUITS = {
    '🍎 apple': {'price': 1.5, 'magic': 'grants wisdom'},
    '🥝 kiwi': {'price': 1.0, 'magic': 'brings good fortune'},
    '🥭 mango': {'price': 5.0, 'magic': 'enhances creativity'},
    '🍐 durian': {'price': 50.0, 'magic': 'bestows strength'},
    '🌟 jackfruit': {'price': 80.0, 'magic': 'reveals secrets'},
    '✨ rambutan': {'price': 1.5, 'magic': 'brings joy'}
}

def display_shop_welcome() -> None:
    print("✨ Welcome to the Enchanted Fruit Emporium! ✨")
    print("Where each fruit holds magical properties...\n")
    
    print("🌟 Today's Magical Selection:")
    print("═" * 50)
    for fruit, info in FRUITS.items():
        print(f"{fruit}: ${info['price']:.2f} - {info['magic']}")
    print("═" * 50)

def calculate_basket_total() -> tuple[float, Dict[str, int]]:
    total_cost = 0
    basket = {}
    
    print("\n🧺 Let's fill your magical basket!")
    for fruit, info in FRUITS.items():
        while True:
            try:
                amount = input(f"How many {fruit} would you like? ")
                if not amount.strip():
                    amount = "0"
                amount = int(amount)
                if amount < 0:
                    print("⚠️ Magic doesn't work with negative numbers!")
                    continue
                break
            except ValueError:
                print("⚠️ Please enter a valid number!")
        
        if amount > 0:
            cost = amount * info['price']
            total_cost += cost
            basket[fruit] = amount
            print(f"✨ Added {amount} {fruit} (${cost:.2f})")
            time.sleep(0.5)
    
    return total_cost, basket

def display_receipt(total: float, basket: Dict[str, int]) -> None:
    print("\n📜 Your Magical Purchase Summary:")
    print("═" * 50)
    if basket:
        for fruit, amount in basket.items():
            print(f"🌟 {amount}x {fruit}")
        print("═" * 50)
        print(f"✨ Total magical investment: ${total:.2f}")
    else:
        print("Your basket is empty! The magic awaits your return...")

def main():
    display_shop_welcome()
    total, basket = calculate_basket_total()
    display_receipt(total, basket)
    
    print("\n🌟 Thank you for visiting the Enchanted Fruit Emporium!")
    print("May your fruits bring you magical fortune! ✨")

if __name__ == '__main__':
    main()