#!/usr/bin/env python3
import time
rounds = 20
i = 0
# this iterates through loop 1 to 20 skipping 13 and states when game over
while i < rounds:
    i += 1
    if i == 13:
        continue
    #message = message + "You got an A"
    #message += "You got an A"
    print(f"Starting round#: {i}")
    time.sleep(0.5)

print("Game over")
