import sys
import time

# ANSI CODE
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def change_color(text, color_code=RESET):
    sys.stdout.write(color_code)
    
    for t in text:
        sys.stdout.write(t)
        sys.stdout.flush()
        time.sleep(0.05)
    
    sys.stdout.write(RESET + "\n")
