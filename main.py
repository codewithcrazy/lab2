import math
from math import *

for i in range(-90, 90, 5):
    x = i / 100
    y = (math.e ** (-2 * x)) * (x**2 + math.sqrt(x + 2)) + sin(x + 2)
    print(x, y)
    