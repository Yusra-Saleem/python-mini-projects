"""
✨ The Magical Square Factory ✨
============================

Ask the user for a number and print its square (the product of the number times itself).

Here's a sample run of the program (user input is in bold italics):

Type a number to see its square: 4

4.0 squared is 16.0
============================
"""

def square_number(number: float) -> float:
    """Returns the square of a number with extra power!"""
    return number * number

def main():
    print("🎲 Welcome to the Number Squaring Spectacular! 🎲")
    print("Where ordinary numbers become extraordinary!\n")

    # Get the number from our brave contestant
    number = float(input("Type a number to see its square: "))
    
    # Transform the number into its mighty squared form
    result = square_number(number)

    # Reveal the mathematical magic
    print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
    print(f"{number} squared is {result}")
    print("*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
    print("\nThank you for checking the power of squares! ⚡")

if __name__ == '__main__':
    main()