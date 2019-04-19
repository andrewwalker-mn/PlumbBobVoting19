minnum = 1000000000
maxnum = 9999999999 #suggested: make these numbers the same number of digits. 
numkeys = 2500 #number of keys you want for the week. MUST BE GREATER THAN DIFFERENCE BETWEEN maxnum AND minnum 

"""Don't touch things below this line"""
keylistlist = []

import random
while len(keylistlist) < numkeys:
  if not random.randint(minnum,maxnum) in keylistlist:
    keylistlist.append(random.randint(minnum,maxnum))




with open("ticketnumbers.csv", "w+") as outf:
  for i in range(len(keylistlist)):
    outf.write(str(random.randint(minnum,maxnum)))
    outf.write("\n")
