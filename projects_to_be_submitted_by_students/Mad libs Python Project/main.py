print("🌟 Welcome to the Mad Libs Adventure! 🌟\n")

# User inputs
name = input("Enter your name: ")
friend = input("Enter your best friend's name: ")
place = input("Enter a magical place: ")
f_animal = input("Enter a wild animal: ")
l_animal = input("Enter a pet animal: ")
object_found = input("Enter an object you find mysterious: ")
emotion = input("Enter an emotion (e.g., excited, scared, joyful): ")
weather = input("Enter a type of weather (e.g., sunny, rainy, stormy): ")
activity = input("Enter a fun activity: ")
feeling = input("Enter a feeling (e.g., love, happiness, fear): ")

# Story
story = f"""
Once upon a time, in the mystical land of {place}, {name} and {friend} set out on an adventure.
The sun was shining brightly, and the weather was {weather}, perfect for an adventure. 
{name} and {friend} were feeling {emotion} as they wandered through the enchanted forest.

While exploring, they stumbled upon a glowing {object_found}. Curious and {emotion}, they decided to take a closer look.
Suddenly, a {f_animal} jumped out from behind a tree, startling them! As they ran for safety, 
{name} tripped over a sleeping {l_animal}, which let out a loud yawn and scolded them for disturbing its nap.

Despite the chaos, they soon realized that the {object_found} held a secret map leading to a hidden treasure. 
Excited, {name} and {friend} continued their journey, ready for their next big adventure. Along the way, they enjoyed 
the {weather} weather and even took some time to {activity} together, strengthening their bond of {feeling}.

As the sun began to set, casting a golden glow over the land, {name} and {friend} finally reached the treasure. 
It was a chest filled with gold, jewels, and a magical artifact that granted them endless adventures and happiness.

Moral of the story: Always be ready for the unexpected, and true friends make every journey worthwhile!  
"""

print("\n✨ Here's your Mad Libs story! ✨\n")
print(story)
