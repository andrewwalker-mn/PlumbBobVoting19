keys = []
tally = {}

with open("ticketnumbers.csv", "r") as keyf: #you're gonna have to change this 
  for line in keyf:
    keys.append(line.rstrip())
    
with open("CSE Week '19 Royalty Vote.csv") as votef: #initializing tally
  for line in votef:
    tally[line.split(",")[3].rstrip()] = 0

print(tally)

with open("CSE Week '19 Royalty Vote.csv") as votef:
  for line in votef:
    if line.split(",")[2][1:-1] in keys:
      print("a")
      tally[line.split(",")[3].rstrip()] += 1
      keys.remove(line.split(",")[2][1:-1])
    else:
      print(line.split(",")[2][1:-1])

with open("cleanresults.csv", "w+") as outf:
  for person in tally:
    outf.write(person)
    outf.write(",")
    outf.write(str(tally[person]))
    outf.write("\n")
