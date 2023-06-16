import random
import math
import matplotlib.pyplot as plt
import numpy

approxline = []
axis = []
axis2 = []
func2 = []
counter = 0
i = 0
while i <= 2:
    func1estimate = (2 * i) / (math.pi * 2)
    approxline.append(func1estimate)
    axis.append(i)
    i = i + 0.01

while i > 2 and i < 10:
    func2estimate = 1 + (2/math.pi)*((i/2)*(1 - math.sqrt(1-(4/(i*i))))- numpy.arcsin(2/i))
    func2.append(func2estimate)
    axis2.append(i)
    i = i + 0.01

plt.plot(axis, approxline, label="Teoretisk funktion för l mindre än eller lika med d")
plt.plot(axis2, func2, label="Teoretisk funktion för l > d")
plt.xlabel("Nålens längd")
plt.ylabel("Sannolikhet för korsning")
plt.legend()
plt.show()