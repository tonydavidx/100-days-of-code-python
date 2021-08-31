from math import radians
import random

seed = int(input("create a seed number: "))
random.seed(seed)

namesAsCsv = input("Give me everybodys names separated by comma ")
names = namesAsCsv.split(", ")

random_name = random.randint(0, len(names)-1)

who = names[random_name]

print(f"{who} is going to buy the meal today!")
