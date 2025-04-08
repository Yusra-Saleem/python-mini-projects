"""
📐 The Pythagoras Power Calculator! 📐
====================================
Discover the magic of right triangles
and unlock the secrets of geometry!
====================================
"""

import math

def calculate_hypotenuse(side_ab: float, side_ac: float) -> float:
    """Calculate the mystical hypotenuse using Pythagoras' ancient wisdom"""
    return math.sqrt(side_ab ** 2 + side_ac ** 2)

def main():
    print("✨ Welcome to the Triangle Temple! ✨")
    print("Where geometry meets magic...\n")
    
    # Gather the sacred measurements
    side_ab = float(input("Enter the length of AB: "))
    side_ac = float(input("Enter the length of AC: "))
    
    # Invoke the power of Pythagoras
    hypotenuse = calculate_hypotenuse(side_ab, side_ac)
    
    # Reveal the mystical result
    print("\n🔮 Ancient geometric calculations intensify 🔮")
    print(f"The length of BC (the hypotenuse) is: {hypotenuse:.2f}")
    print("\nThank you for exploring the wonders of geometry! ⚡")

if __name__ == '__main__':
    main()