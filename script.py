import csv
import random

with open('names.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    
lucky_number = random.randint(0, len(data)-1)

winner = data[lucky_number]
print(winner)
