"""
Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

Here's a sample run of the program:

What's your favorite animal? **_cow_**

My favorite animal is also cow!


------------------------------------------------
A delightfully agreeable bot that shares your excellent taste in animals!
"""

def main():
    print("🌟 Hello! I'm the Most Agreeable Bot in the Universe! 🌟")
    print("I bet we have the same taste in animals...\n")
    
    animal: str = input("What's your favorite animal? ")
    
    print(f"\nGASP 😲 NO WAY!")
    print(f"My favorite animal is also {animal}! 🎉")
    print(f"\n{get_animal_emoji()} {animal.upper()} FANS UNITE! {get_animal_emoji()}")

def get_animal_emoji() -> str:
    """Returns a friendly emoji for extra enthusiasm"""
    return "🦋"

if __name__ == '__main__':
    main()