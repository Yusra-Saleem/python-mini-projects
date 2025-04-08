import random
import string

# Hangman ASCII Art for different attempts left
HANGMAN_PICS = [
    '''
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
          ===''', 
    '''
       +---+
       |   |
       O   |
      /|\\  |
      /    |
          ===''', 
    '''
       +---+
       |   |
       O   |
      /|\\  |
           |
          ===''', 
    '''
       +---+
       |   |
       O   |
      /|   |
           |
          ===''', 
    '''
       +---+
       |   |
       O   |
       |   |
           |
          ===''', 
    '''
       +---+
       |   |
       O   |
           |
           |
          ===''', 
    '''
       +---+
       |   |
           |
           |
           |
          ==='''
]

# Words with categories and hints
WORDS_WITH_HINTS = {
    "pizza": ("Food", "A popular Italian dish with cheese & toppings"),
    "banana": ("Food", "A yellow fruit that monkeys love"),
    "burger": ("Food", "A sandwich with a patty, often served with fries"),
    "pasta": ("Food", "An Italian dish made from wheat and served with sauce"),
    "icecream": ("Food", "A frozen sweet dessert, often in different flavors"),
    "sandwich": ("Food", "A meal between two slices of bread"),
    "sushi": ("Food", "A Japanese dish with rice and seafood"),
    "chocolate": ("Food", "A sweet treat made from cocoa"),
    "popcorn": ("Food", "A popular snack at the movies"),
    "strawberry": ("Food", "A red fruit with seeds on the outside"),
    "jacket": ("Clothing", "Worn in winter to stay warm"),
    "shoes": ("Clothing", "Worn on feet for walking and running"),
    "jeans": ("Clothing", "Denim pants that are always in style"),
    "gloves": ("Clothing", "Worn on hands during cold weather"),
    "socks": ("Clothing", "Worn on feet inside shoes"),
    "hat": ("Clothing", "A head accessory, can be for fashion or warmth"),
    "scarf": ("Clothing", "Worn around the neck in winter"),
    "tie": ("Clothing", "A formal accessory for the neck"),
    "shorts": ("Clothing", "Worn in summer to keep cool"),
    "tiger": ("Animal", "A big wild cat with orange and black stripes"),
    "elephant": ("Animal", "The largest land animal with a trunk"),
    "giraffe": ("Animal", "The tallest animal with a long neck"),
    "lion": ("Animal", "Known as the 'King of the Jungle'"),
    "dolphin": ("Animal", "A smart marine animal that loves to jump"),
    "panda": ("Animal", "A black and white bear that loves bamboo"),
    "zebra": ("Animal", "A striped animal found in Africa"),
    "kangaroo": ("Animal", "An animal that hops and carries babies in a pouch"),
    "owl": ("Animal", "A nocturnal bird known for its hoots"),
    "octopus": ("Animal", "A sea creature with eight tentacles"),
    "football": ("Game", "A sport played with a round ball and two goals"),
    "chess": ("Game", "A board game played with black and white pieces"),
    "cricket": ("Game", "A popular bat-and-ball game"),
    "badminton": ("Game", "A fast-paced racket sport"),
    "hockey": ("Game", "A sport played on ice or field with sticks"),
    "basketball": ("Game", "A sport where players shoot a ball into a hoop"),
    "volleyball": ("Game", "A game played with a net and a ball"),
    "tennis": ("Game", "A sport played on a court with rackets"),
    "poker": ("Game", "A card game that requires strategy and luck"),
    "golf": ("Game", "A sport played on a vast green field with clubs"),
    "laptop": ("Object", "A portable computer used for work and gaming"),
    "guitar": ("Object", "A musical instrument with strings"),
    "camera": ("Object", "Used to capture moments and pictures"),
    "clock": ("Object", "Used to tell time"),
    "headphones": ("Object", "Used to listen to music"),
    "microwave": ("Object", "Used to heat food quickly"),
    "keyboard": ("Object", "A device used to type on a computer"),
    "bicycle": ("Object", "A two-wheeled vehicle that requires pedaling"),
    "drums": ("Object", "A musical instrument played by beating with sticks"),
    "wallet": ("Object", "Used to carry money and cards"),
    "beach": ("Place", "A sandy location by the ocean"),
    "mountain": ("Place", "A tall natural elevation with peaks"),
    "desert": ("Place", "A dry, sandy, and hot region"),
    "jungle": ("Place", "A dense forest with wild animals"),
    "library": ("Place", "A quiet place with lots of books"),
    "museum": ("Place", "A place where historical artifacts are kept"),
    "airport": ("Place", "Where planes take off and land"),
    "theater": ("Place", "Where movies and plays are shown"),
    "zoo": ("Place", "A place where animals are kept for public viewing"),
    "market": ("Place", "Where people buy and sell goods")
}

def get_valid_word():
    """Returns a random word, its category, and hint."""
    word, (category, hint) = random.choice(list(WORDS_WITH_HINTS.items()))
    return word.upper(), category, hint

def reveal_random_letters(word, count):
    """Reveals 'count' random letters in the word as hints."""
    word_letters = list(word)
    revealed = random.sample(word_letters, min(count, len(set(word))))  # Pick unique letters
    return set(revealed)

def hangman():
    word, category, hint = get_valid_word()  # Choose a random word, category, and hint
    word_letters = set(word)  # Unique letters in the word
    alphabet = set(string.ascii_uppercase)  # All uppercase letters
    used_letters = set()  # Track guessed letters
    attempts = 6  # Maximum incorrect attempts

    # Generate 1-3 hints
    hint_count = random.randint(1, 3)
    hint_letters = reveal_random_letters(word, hint_count)
    used_letters.update(hint_letters)  # Add hint letters to guessed letters
    word_letters -= hint_letters  # Remove revealed letters from unguessed letters

    print("\nWelcome to Hangman! Can you guess the word?")
    print(f"Category: {category}")
    print(f"Hint: {hint}")
    print(f"Free Clue: {hint_count} letters are revealed!\n")

    while len(word_letters) > 0 and attempts > 0:
        print(HANGMAN_PICS[6 - attempts])  # Show the hangman state
        print(f"\nAttempts left: {attempts}")
        print(f"Used letters: {' '.join(sorted(used_letters))}")

        # Display the word with guessed letters
        word_display = [letter if letter in used_letters else "_" for letter in word]
        print("\nWord: ", " ".join(word_display))

        # Get user input
        user_letter = input("\nGuess a letter: ").upper()

        # Validate input
        if len(user_letter) != 1 or user_letter not in alphabet:
            print("Invalid input! Please enter a single letter.")
            continue

        if user_letter in used_letters:
            print("You've already guessed that letter. Try again!")
            continue

        used_letters.add(user_letter)  # Add to guessed letters

        if user_letter in word_letters:
            word_letters.remove(user_letter)
            print(f"Correct! '{user_letter}' is in the word!")
        else:
            attempts -= 1
            print(f"Oops! '{user_letter}' is NOT in the word!")

    # End of game results
    print(HANGMAN_PICS[6 - attempts])  # Show final hangman state

    if len(word_letters) == 0:
        print(f"\n🎉 Congratulations! You guessed the word: {word} 🎉")
    else:
        print(f"\n💀 Game Over! The word was: {word} 💀")

    # Ask to play again
    play_again = input("\n🔄 Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        hangman()
    else:
        print("\n👋 Thanks for playing! See you next time!")

# Start the game
hangman()
