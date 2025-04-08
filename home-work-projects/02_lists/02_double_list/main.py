"""
✨ The Magical Number Doubler ✨
============================
Where numbers discover their double power!
============================
"""

def double_list(numbers: list[int]) -> list[int]:
    """Transform each number into its magical double!"""
    return [number * 2 for number in numbers]

def display_transformation(original: list[int], doubled: list[int]) -> None:
    print("Original Numbers:", " → ".join(map(str, original)))
    print("       Doubled:", " → ".join(map(str, doubled)))

def main():
    print("🎭 Welcome to the Number Transformation Chamber! 🎭")
    print("Watch as we double the power of each number...\n")

    numbers = [1, 2, 3, 4]
    doubled_numbers = double_list(numbers)
    
    print("✨ *Magic transformation in progress* ✨\n")
    display_transformation(numbers, doubled_numbers)
    print("\n🌟 The transformation is complete! 🌟")

if __name__ == '__main__':
    main()