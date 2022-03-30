import time
import sys

def talking(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        if (char == "\n"):
            time.sleep(1)
        else:
            time.sleep(0.4)

talking("hello world!\nBye Bye World!")  