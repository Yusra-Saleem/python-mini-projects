"""
🔢 The Magical Division Adventure! 🔢
===================================
Where numbers split and remainders dance!
===================================
"""

def calculate_division(dividend: int, divisor: int) -> tuple[int, int]:
    return dividend // divisor, dividend % divisor

def main():
    print("✨ Welcome to the Division Kingdom! ✨")
    print("Where numbers reveal their secrets...\n")
    
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))
    
    quotient, remainder = calculate_division(dividend, divisor)
    
    print("\n🎲 Mathematical magic happens 🎲")
    print(f"The result of this division is {quotient} with a remainder of {remainder}")
    print("\n🌟 Thanks for diving into division with us! 🌟")

if __name__ == '__main__':
    main()