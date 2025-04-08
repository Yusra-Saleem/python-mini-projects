import random
import time

def guess():
    random_Num = random.randint(1, 10)
    attempts = 0
    max_attempts = 3

    print("\n🎯 Welcome to the ULTIMATE 1-10 Guessing Game! 🎯")
    print("\n🤖 AI: I have picked a number between 1 and 10.")
    print(f"🔮 You have only {max_attempts} attempts. Guess wisely... or face the consequences! ⚔️\n")

    while attempts < max_attempts:
        try:
            user_guess = int(input("🎲 Enter your guess (1-10): "))
            if user_guess < 1 or user_guess > 10:
                print("❌ Out of range! Please pick a number between 1 and 10.")
                continue
        except ValueError:
            print("❌ That’s not a number! Try again. 😅")
            continue

        attempts += 1

        if user_guess < random_Num:
            print("📉 Too low! Think bigger! 🔼")
        elif user_guess > random_Num:
            print("📈 Too high! Think smaller! 🔽")
        else:
            print("🎉🎊 BOOM! You guessed it right! You’re a legend! 🏆🎖️\n")
            return

        if attempts < max_attempts:
            print(f"💡 HINT: You have {max_attempts - attempts} attempts left!\n")
        else:
            print("\n💀 GAME OVER! You ran out of attempts! 💀")
            print(f"😏 The correct number was {random_Num}. Better luck next time! 🍀\n")

# Start the game
guess()
