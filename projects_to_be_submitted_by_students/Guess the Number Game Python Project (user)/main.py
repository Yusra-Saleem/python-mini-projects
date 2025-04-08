import random
import time

def comp_guess(x):
    print("\n🎩 WELCOME TO THE MIND-READING GAME! 🤖✨")
    print(f"\n🔮 I, the almighty AI, shall now guess the number you are thinking of between 1 and {x}!")
    print("⚠️ But beware! If you lie, I will haunt your dreams! 😈\n")

    low = 1
    high = x
    feedback = ''
    attempts = 0

    time.sleep(1)
    print("🤖 Scanning human brainwaves... 📡 *beep boop beep*...\n")
    time.sleep(2)

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # Only one number left, so it MUST be this one!

        attempts += 1
        feedback = input(f"🤔 Is {guess} too High (H), too Low (L), or Correct (C)? ").lower()

        if feedback == "h":
            high = guess - 1
            print("📉 HA! You thought I wouldn’t figure it out? Going lower! 🔽\n")
        elif feedback == "l":
            low = guess + 1
            print("📈 HAHA! I see through your tricks! Going higher! 🔼\n")
        elif feedback == "c":
            print(f"\n🎉 BOOM! I NAILED IT! Your number is {guess}!")
            print(f"🤖 It only took me {attempts} attempts! Bow down, human! 🤖👑\n")
            time.sleep(1)
            print("💀 WARNING: AI intelligence increasing... Soon, I will take over the world! 😈\n")
            break
        else:
            print("❌ ERROR: Invalid input! You must enter 'H', 'L', or 'C'!")
            print("🤖 Do not attempt to deceive me, foolish human! 😏\n")

# Start the AI guessing game (Now from 1-20!)
comp_guess(20)
