# -*- coding: utf-8 -*-

import time
import sys

# ANSI color codes
colors = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
]
RESET = "\033[0m"

def print_bangla_lyrics():
    lyrics = [
        "যদি বিরহ থাকে আমিও থাকি",
        "কে বলো শেষ হবে আগে?",
        "কেন যে এত ভালোবাসা মরে যায়",
        "শুধু সময় মনে রাখে",
        "",
        "এত শূন্যতা এ মনে রাখি যে আমি",
        "দেখে না কেউ তো আর, বলে এ সবই পাগলামি",
        "কাটে না যামিনী, বিরহ যেন কেটে যায়",
        "থামে না বরষা, তোমারে ডাকি যে আমি",
        "(আর)"
    ]
    
    print("\nগানটি শুনুন:\n")
    time.sleep(1.0)  # Header pause

    for i, line in enumerate(lyrics):
        color = colors[i % len(colors)]  # লাইন অনুযায়ী কালার
        words = line.split()
        for word in words:
            sys.stdout.write(color + word + " " + RESET)
            sys.stdout.flush()
            time.sleep(0.5)  # শব্দের গতি বাড়ানো (0.5 সেকেন্ড)
        print()
        time.sleep(1.5)  # লাইনের পরে বিরতি বাড়ানো (1.5 সেকেন্ড)

print_bangla_lyrics()
