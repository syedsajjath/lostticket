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
    
    #print(availlist)
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
        #print (availlist)
    if seatlist[seats - 1] == seats:
        #print("good")
        goodcount += 1
    else:
        #print("Bad")
        badcount += 1
    sampleset.append(seatlist)
#print (sampleset)
print (goodcount/(goodcount + badcount))
#print (badcount)