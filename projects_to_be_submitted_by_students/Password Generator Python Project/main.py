import random
import string

def generate_password(length, use_upper, use_digits, use_special):
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ""
    digits = string.digits if use_digits else ""
    special = "!@#$%^&*()-_=+" if use_special else ""

    all_chars = lower + upper + digits + special
    
    if not all_chars:
        print("❌ Error: No character set selected! Please enable at least one option.")
        return None
    
    # Ensure password contains at least one character from each selected category
    password = []
    if use_upper:
        password.append(random.choice(upper))
    if use_digits:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special))

    # Fill the remaining length with random choices
    password.extend(random.choices(all_chars, k=length - len(password)))
    
    # Shuffle to make it more secure
    random.shuffle(password)

    return "".join(password)

# Welcome message
print("🔐 Welcome to the Ultimate Password Generator! 🔐")

try:
    length = int(input("\n🔢 Enter the desired password length (min 4): "))
    
    if length < 4:
        print("❌ Password length must be at least 4 characters for security reasons.")
    else:
        # User preferences
        use_upper = input("🔠 Include uppercase letters? (y/n): ").strip().lower() == "y"
        use_digits = input("🔢 Include numbers? (y/n): ").strip().lower() == "y"
        use_special = input("✨ Include special characters? (y/n): ").strip().lower() == "y"

        # Generate password
        password = generate_password(length, use_upper, use_digits, use_special)

        if password:
            print(f"\n✅ Your Secure Password: 🔒 {password} 🔒")
            print("\n📌 Remember to save it securely!")

except ValueError:
    print("❌ Invalid input! Please enter a valid number for the password length.")
