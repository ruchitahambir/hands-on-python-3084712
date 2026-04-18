import csv
# Open and read your new file
with open('moon.csv','r') as a:
  reader = csv.DictReader(a)
  moon = list(reader)
print (f"---Loaded {len(moon)} space Moon mission ---\n")

# Practice 1: Print all mission names
print("All Mission Names:")
for a in moon:
    print(f" - {a['mission_name']}")

# Practice 2: Filter for missions to the 'Moon'
print("\nMoon Missions:")
for m in moon:
    if m['destination'] == 'Moon':
        print(f" > {m['mission_name']} was launched in {m['year']}")

# Practice 3: Check for failures
print("\nFailed Missions:")
for m in moon:
    if m['status'] == 'Failure':
        print(f" ! Alert: {m['mission_name']} to {m['destination']} failed.")
