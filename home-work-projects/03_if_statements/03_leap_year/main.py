"""
🌟 The Mystical Calendar Oracle 🌟
===============================
Peer into the fabric of time itself
and discover the secrets of leap years!
===============================
"""

import time

def check_leap_year(year: int) -> bool:
    """Consults the ancient calendar scrolls"""
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False

def display_mystical_message(year: int, is_leap: bool) -> None:
    """Reveals the prophecy with magical flourish"""
    print("\n✨ Consulting the temporal spirits...")
    time.sleep(1)
    
    print("🌙 The stars align...")
    time.sleep(0.5)
    
    print("📜 The ancient scrolls reveal...")
    time.sleep(1)
    
    if is_leap:
        print(f"""
        ⭐️ BEHOLD! The year {year} is blessed! ⭐️
        It bears the mark of the leap year,
        granting it 366 days of magical power!
        February shall receive the gift of
        an extra day of enchantment!
        """)
    else:
        print(f"""
        🌑 The year {year} follows the regular
        flow of time, with 365 days in its cycle.
        February remains at its usual length,
        as the cosmic balance dictates.
        """)

def main():
    print("🎭 Welcome, Time Seeker! 🎭")
    print("To the Mystical Calendar Oracle...\n")
    
    try:
        year = int(input("🔮 Speak the year you wish to divine: "))
        
        if year < 0:
            print("\n⚠️ The ancient scrolls cannot read years before time itself!")
            return
            
        is_leap = check_leap_year(year)
        display_mystical_message(year, is_leap)
        
        print("\n✨ The prophecy is complete! ✨")
        
    except ValueError:
        print("\n⚠️ That is not a year recognized by the temporal spirits!")

if __name__ == '__main__':
    main()