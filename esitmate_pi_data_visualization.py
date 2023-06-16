import random
import math
import matplotlib.pyplot as plt

approxline = []

axis = []
straight = []
counter = 0
i = 0

while i < 100000:
    pos = random.uniform(0, 1)
    angle = math.radians(random.uniform(0, 90))
    length = math.sin(angle)
    if pos + length > 1:
        counter += 1
    i += 1
    if counter != 0:
        x = 2 * i/counter
        approxline.append(x)
        axis.append(i)
        straight.append(math.pi)

plt.plot(axis, approxline, label="approximation")
plt.plot(axis, straight, label="pi")
plt.xlabel("Antal kastade nålar")
plt.ylabel("Sannolikheten för korsning")
plt.legend()
plt.show()