import os
import random

file_names = os.listdir("puzzles")

for i, f in enumerate(file_names):
    print(str(i+1) + ") " + f - ".txt")

choice = input("Which list would you like? ")
choice = int(choice) - 1

file = "puzzles/" + file_names[choice]
print(file)

with open(file, 'r') as f:
    lines = f.read().splitlines()

print(lines)

category = lines[0]
puzzle = random.choice(lines[1:])

print(category)
print(puzzle)
