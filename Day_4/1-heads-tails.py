from math import radians
import random

seed = int(input("create a seed number: "))
random.seed(seed)

random_num = random.randint(0, 1)

if random_num == 0:
    print("Heads")
else:
    print("Tails")
