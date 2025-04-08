"""
📏 The Magical Measurement Transformer 📏
=======================================
Turn those feet into inches with style!
Let's make measurement conversion fun!
=======================================
"""

INCHES_IN_FOOT = 12  # The magical conversion number! ✨

def convert_to_inches(feet: float) -> float:
    """Transform feet into inches with mathematical magic!"""
    return feet * INCHES_IN_FOOT

def main():
    print("🌟 Welcome to the Imperial Length Laboratory! 🌟")
    print("Where feet become inches in the blink of an eye!\n")
    
    
    feet = float(input("Enter number of feet: "))
   
    inches = convert_to_inches(feet)
    
 
    print(f"{feet} feet is equal to...")
    print(f"🎯 {inches:,.2f} magical inches! 🎯")
    
    print("\nThank you for exploring measurements with us! 🎊")

if __name__ == '__main__':
    main()