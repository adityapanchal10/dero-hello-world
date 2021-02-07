from random import randint, seed
import time

hello_world = "Hello World!"
msg = ""
i = 0
while(msg != hello_world):
    char = chr(randint(32, 126))
    print(msg + char)
    if (hello_world[i] == char):
        msg += char
        i += 1
    time.sleep(1)
print(msg)