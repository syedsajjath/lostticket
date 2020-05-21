from random import seed
from random import randint

seatlist = []
availlist = []
sampleset = []

goodcount = 0
badcount = 0
samplesize = 100000
seats = 100

for j in range (samplesize):
    availlist.clear()
    seatlist.clear()

    for i in range (1,seats + 1):
        availlist.append(i)
    
    start = randint(1, seats)
    seatlist.append(start)
    availlist.remove(start)        

    for i in range(2, seats + 1):
        if i in availlist:
            seatlist.append (i)
            availlist.remove (i)
        else:
            randomseat = availlist[randint(0,len(availlist) - 1)] 
            seatlist.append(randomseat)
            availlist.remove(randomseat)
        
    if seatlist[seats - 1] == seats:
        #print("good")
        goodcount += 1
    else:
        badcount += 1
        
    sampleset.append(seatlist)

print ("Success: " , goodcount)
print ("Failed: ", badcount)
print ("Probability: ", goodcount/(goodcount + badcount))
