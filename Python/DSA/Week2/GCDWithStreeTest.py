#Uses python3

import random

def GCDSlow(firstnumber, secondnumber):
    best = 0

    for i in range(1, (firstnumber + secondnumber)):
        if firstnumber % i == 0 and secondnumber % i == 0:
            best = i

    return best

def GCDFast(firstnumber, secondnumber):

    if secondnumber == 0:
        return firstnumber
    else:
        reminder = firstnumber % secondnumber
    return GCDFast(secondnumber, reminder)

rightresultfound = 1

while rightresultfound:
    firstnumber = random.randint(1, 10000)
    secondnumber = random.randint(1, 10000)
    fastresult = GCDFast(firstnumber, secondnumber)
    slowresult = GCDSlow(firstnumber, secondnumber)

    if fastresult == slowresult:
        print("OK")
    else:
        print("NOT OK", firstnumber, secondnumber)
        rightresultfound = 0



