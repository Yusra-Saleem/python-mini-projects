"""
🌙 The Mysterious Tale Weaver 🌙
============================
Creating enchanted stories from your imagination!
============================
"""

STORY_TEMPLATE = """In the depths of an ancient forest, a {adjective} {noun} discovered a mysterious portal 
shimmering with starlight. As they stepped through, they gained the power to {verb}! 
The magical creatures of the forest watched in awe as {noun} danced with their new abilities.
"""

STORY_MIDDLE = f"""Deep in the heart of the enchanted woods, whispers spread about the {'{noun}'} 
who could {'{verb}'} with extraordinary grace. Their {'{adjective}'} presence brought hope 
to all who witnessed their magic."""

STORY_END = """And so, beneath the eternal stars, a new guardian of the magical realm emerged,
their legend destined to inspire dreamers for generations to come... ✨🌟"""

def create_story(adjective: str, noun: str, verb: str) -> str:
    story_parts = [
        STORY_TEMPLATE.format(adjective=adjective, noun=noun, verb=verb),
        STORY_MIDDLE.format(noun=noun, verb=verb, adjective=adjective),
        STORY_END
    ]
    return "\n".join(story_parts)

def main():
    print("✨ Welcome to the Chamber of Mysteries! ✨")
    print("Let's weave a tale of wonder and magic...\n")

    print("🌿 Hint: Describe your character (like 'moonlit' or 'ethereal')")
    adjective = input("Share a mystical adjective: ")
    
    print("\n🎭 Hint: Who is our mysterious hero? (like 'dragonkin' or 'stardancer')")
    noun = input("Name the legendary being: ")
    
    print("\n⚡ Hint: What magical power awaits? (like 'weave-starlight' or 'whisper-to-dragons')")
    verb = input("Reveal their mystical ability: ")

    print("\n🌌 *Ancient magic stirs* 🌌")
    print("\n📜 Your Mystical Tale:")
    print(create_story(adjective, noun, verb))
    print("\n✨ Thank you for sharing in this magical journey! ✨")

if __name__ == '__main__':
    main()