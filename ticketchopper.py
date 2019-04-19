l = []
numinaline = 20
with open("ticketnumbers.csv", "r") as inf:
  with open("choppedtix.csv", "w+") as outf:
    for line in inf:
      l.append(line.split("\n")[0])
    counter = 0
    for item in l:
      if counter < numinaline-1: 
        outf.write(str(item)+",")
        counter+=1
      else:
        counter = 0
        outf.write("\n")
        for num in range(0,numinaline):
          outf.write("z.umn.edu/CSEVote19"+",")
        outf.write("\n")
        outf.write(str(item)+",")
