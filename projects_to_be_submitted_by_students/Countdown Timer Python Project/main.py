import time
import sys

def countdown(t):
    print("\n⏳ Countdown Timer Started! ⏳\n")
    
    while t > 0:
        mins, secs = divmod(t, 60)  # Convert seconds to minutes and seconds
        timer = f"{mins:02d}:{secs:02d}"  # Format as MM:SS
        sys.stdout.write(f"\r⏰ Time Left: {timer} ")  # Print on the same line
        sys.stdout.flush()
        time.sleep(1)  # Delay for 1 second
        t -= 1  # Reduce time by 1 second

    print("\n🎉 Timer Completed! 🎉")
    print("✨ Time’s up! Hope you had a productive session. 🚀")

# User Input with better prompt
try:
    t = int(input("⏳ Enter the countdown time in seconds: "))
    if t <= 0:
        print("❌ Please enter a positive number!")
    else:
        countdown(t)
except ValueError:
    print("❌ Invalid input! Please enter a valid number.")
