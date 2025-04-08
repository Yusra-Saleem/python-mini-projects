"""
⏰ Time Explorer's Calculator ⏰
============================
Journey through the sands of time
to discover the secrets of a year!
============================
"""

DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MIN_PER_HOUR = 60
SEC_PER_MIN = 60

def calculate_seconds() -> int:
    return DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN

def main():
    print("✨ Welcome to the Time Explorer's Laboratory! ✨")
    print("Calculating the heartbeats of a year...\n")
    
    seconds = calculate_seconds()
    
    print("🌟 *Time machines whirring* 🌟")
    print(f"\nIncredible discovery!")
    print(f"There are {seconds:,} seconds in a year!")
    print("\n⚡ Time is precious, use it wisely! ⚡")

if __name__ == '__main__':
    main()