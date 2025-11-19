import time
import sys

def print_bangla_lyrics():
    lyrics = [
        "যদি বিরহ থাকে আমিও থাকি",
        "কে বলো শেষ হবে আগে?",
        "কেন যে এত ভালোবাসা মরে যায়",
        "শুধু সময় মনে রাখে",
        "",
        "[Chorus: Ankan Kumar]",
        "এত শূন্যতা এ মনে রাখি যে আমি",
        "দেখে না কেউ তো আর, বলে এ সবই পাগলামি",
        "কাটে না যামিনী, বিরহ যেন কেটে যায়",
        "থামে না বরষা, তোমারে ডাকি যে আমি",
        "(আর)"
    ]
    
    print("\nগানটি শুনুন:\n")
    time.sleep(1.0)  # Header pause

    for line in lyrics:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)  # Letter-by-letter delay
        print()  # Newline after each line
        time.sleep(0.5)  # Line-by-line delay

print_bangla_lyrics()
