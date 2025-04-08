"""
✨ Number Symphony ✨
==================
Where numbers dance together
to create mathematical magic!
==================
"""

def add_many_numbers(numbers: list[int]) -> int:
    return sum(numbers)

def main():
    print("🎭 Welcome to the Number Symphony! 🎭")
    print("Watch as we orchestrate numerical harmony...\n")
    
    numbers = [1, 2, 3, 4, 5]
    total = add_many_numbers(numbers)
    
    print("✨ *Mathematical magic in progress* ✨")
    print(f"\nOur magical numbers: {numbers}")
    print(f"Their harmonious sum: {total}")
    print("\n🌟 Thank you for joining our mathematical performance! 🌟")

if __name__ == '__main__':
    main()