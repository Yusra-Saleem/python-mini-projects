"""
🔺 Triangle Perimeter Adventure! 🔺
Join us on a magical geometric journey to discover
the mysterious perimeter of your triangle!
"""

def calculate_perimeter(side1: float, side2: float, side3: float) -> float:
    return side1 + side2 + side3

def main():
    print("⭐️ Welcome to the Triangle Territory! ⭐️")
    print("Let's measure your triangle's magnificent boundary...\n")

    # Gather the mystical measurements
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    # Calculate the grand total
    perimeter = calculate_perimeter(side1, side2, side3)

    print("\n✨ Drumroll please... ✨")
    print(f"The perimeter of the triangle is {perimeter}")
    print("\nThanks for exploring the world of triangles with us! 🎉")

if __name__ == '__main__':
    main()