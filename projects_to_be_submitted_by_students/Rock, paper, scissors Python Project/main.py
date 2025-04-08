import random
import time

def play():
    print("\n🎮 WELCOME TO THE LEGENDARY DUEL: ROCK 🪨, PAPER 📜, SCISSORS ✂️!\n")
    time.sleep(1)
    print("🔥 Think you're smarter than an AI? Let's see about that! 🤖💥\n")
    
    user = input("👉 Choose your weapon: 'R' for Rock 🪨, 'P' for Paper 📜, 'S' for Scissors ✂️: ").upper()
    
    if user not in ['R', 'P', 'S']:
        print("\n❌ ERROR 404: Brain Not Found! 🧠💨 Please choose R, P, or S like a normal human. 😆\n")
        return play()  # Restart the game if input is invalid

    time.sleep(1)
    print("\n🤖 AI is scanning the matrix... calculating your weakness...\n")
    time.sleep(2)

    computer = random.choice(['R', 'P', 'S'])
    print(f"💻 AI has made its move... It chose: {computer}\n")

    if user == computer:
        print(f"😲 DRAW! Both chose {computer}! The universe is in balance... for now. 🌍⚖️\n")
    elif is_win(user, computer):
        print("🎉 VICTORY! 🏆 You have outsmarted the AI! Enjoy your glory before the robots take over! 🤖😈\n")
    else:
        print("😢 YOU LOSE! The AI chuckles at your failure. Try again, puny human! 💀💔\n")

def is_win(player, opponent):
    """Returns True if the player beats the opponent"""
    return (player == 'R' and opponent == 'S') or \
           (player == 'S' and opponent == 'P') or \
           (player == 'P' and opponent == 'R')

# Start the battle
play()
