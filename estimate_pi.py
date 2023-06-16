import random
import math
counter = 0
i = 0
while i < 1000000:
    pos = random.uniform(0, 1)
    angle = math.radians(random.uniform(0, 90))
    length = math.sin(angle)
    if pos + length > 1:
        counter += 1
    i += 1
    if i == 100 or i == 10000 or i == 1000000:
        x = 2 * i / counter
        print("", x)