# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


teams = []

filename = sys.argv[1]
with open(filename) as file:
    reader = csv.DictReader(file)
    for i in reader:
        i["rating"] = int(i["rating"])
        teams.append(i)

wn = []
ran = random.randint(1, 16)
for i in range(len(teams)):
   
print(teams[ran])
print(wn)
