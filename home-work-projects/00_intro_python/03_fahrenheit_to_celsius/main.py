"""
Temperature Converter! 🌡️
Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!
Convert Fahrenheit to Celsius with style!
"""

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Converts Fahrenheit temperature to Celsius"""
    return (fahrenheit - 32) * 5.0/9.0

def main():
    print("🌡️ Welcome to the Fantastic Temperature Converter! 🌡️")
    print("Let's turn that Fahrenheit into Celsius magic! ✨\n")
    
    
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    

    if celsius > 30:
        emoji = "🔥"
        message = "Whew, that's hot!"
    elif celsius < 0:
        emoji = "❄️"
        message = "Brrr, bring a jacket!"
    else:
        emoji = "👌"
        message = "Perfect weather!"
    
   
    print(f"\n{emoji} Temperature Report {emoji}")
    print(f"Temperature: {fahrenheit}°F = {celsius}°C")
    print(f"{message}")

if __name__ == '__main__':
    main()