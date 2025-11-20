import time
import sys

def print_lyrics():
    lyrics = [
        "haanthon ko sambhale mere haathon main",
        "kaise haathon ko sambhale mere haathon main..",
        "jab tak neend na aaye, inn lakeeron main..",
        "baathein ho.......",
    ]
    
    delays = [1.0, 0.1, 1.12, 0.9]

    print("Arz kya hai?.......:\n")
    time.sleep(1.4)
    
    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)     
            sys.stdout.flush()
            time.sleep(0.05)          
        
        print()                         
        time.sleep(delays[i])           


print_lyrics()