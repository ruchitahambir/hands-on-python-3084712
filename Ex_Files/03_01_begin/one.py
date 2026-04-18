import csv

with open('moon.csv','r') as a:
  reader = csv.DictReader(a)
  moon = list(reader)

print (f"---Loaded {len(moon)} space Moon mission ---\n")