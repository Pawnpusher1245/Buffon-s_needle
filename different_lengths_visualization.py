import random
import math
import matplotlib.pyplot as plt
approxline = []
axis = []
needle = 0.01
counter = 0
i = 0
j = 0
while j < 500:
    while i < 50000:
        pos = random.uniform(0, 1)
        angle = math.radians(random.uniform(0, 90))
        length = math.sin(angle)

        if pos + needle * length > 1:
            counter += 1

        i += 1

    x = counter / i
    approxline.append(x)
    axis.append(2 * needle)
    j += 1
    needle = needle + 0.01
    counter = 0
    i = 0
plt.plot(axis, approxline, label="Korsande nålar/Kastade nålar")

plt.xlabel("Värde på l")
plt.ylabel("Sannolikhet för korsning")

plt.legend()

plt.show()