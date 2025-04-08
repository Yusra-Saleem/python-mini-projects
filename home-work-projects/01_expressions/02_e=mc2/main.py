"""
⚡️ Einstein's Energy Explorer ⚡️
===============================
Turn ordinary mass into extraordinary energy!
Let's discover the power hidden in matter...
===============================
"""

# The cosmic speed constant! ⚡️
SPEED_OF_LIGHT = 299792458  # meters per second

def calculate_energy(mass: float) -> float:
    """Transforms mass into energy using Einstein's famous equation"""
    return mass * (SPEED_OF_LIGHT ** 2)

def main():
    print("🔬 Welcome to Einstein's Energy Laboratory! 🔬")
    print("Where E = mc² comes alive!\n")
    
    # Get mass input from our brave scientist
    mass = float(input("Enter kilos of mass: "))
    
    # Calculate the incredible energy
    energy = calculate_energy(mass)
    
    # Present the results with style
    print("\n🌟 Computing quantum transformation... 🌟")
    print("\nE = mc²...")
    print(f"Mass: {mass} kg")
    print(f"Speed of Light: {SPEED_OF_LIGHT} m/s")
    print(f"\n✨ INCREDIBLE! That creates:")
    print(f"{energy:,.2f} joules of energy!")
    
    print("\n🎉 Thank you for exploring the universe with us! 🎉")

if __name__ == '__main__':
    main()