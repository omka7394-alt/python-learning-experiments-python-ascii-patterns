import os
import time
import random

colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
reset = '\033[0m'

def draw_tree():
    os.system('clear')
    print("\n" * 2)
    lines = 10
    for i in range(lines):
        spaces = " " * (lines - i - 1)
        stars = ""
        for j in range(2 * i + 1):
            if random.random() < 0.3:
                color = random.choice(colors)
                stars += f"{color}*{reset}"
            else:
                stars += f"\033[92m▲{reset}"
        print(spaces + stars)
    print(" " * (lines - 2) + "\033[43m  \033[0m")
    print(" " * (lines - 2) + "\033[43m  \033[0m")

try:
    while True:
        draw_tree()
        time.sleep(0.4)
except KeyboardInterrupt:
    print("\nStopped!")
