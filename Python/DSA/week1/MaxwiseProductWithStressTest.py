#Uses python3

import random

def MaxWiseProductFast(inputList):
    firstmax = 0
    secondmax = 0
    firstmaxindex = 0
    for i in range(len(inputList)):
        if inputList[i] > firstmax:
            firstmax = inputList[i]
            firstmaxindex = i

    for j in range(len(inputList)):
        if firstmaxindex != j:
            if inputList[j] > secondmax:
                secondmax = inputList[j]

    return firstmax * secondmax

def MaxWiseProductSlow(inputList):
    product = 0
    for i in range(len(inputList)):
        for j in range(i + 1, len(inputList)):
            product = max(product, inputList[i] * inputList[j])
    return product

def MaxWiseProductStressTest():
    randomn = random.randint(1, 10)
    print(randomn)
    randominputlist = []
    for i in range(randomn):
        randominputlist.append(int(random.randint(0, 200000)))
    return randominputlist


n = int(input())

a = [int(x) for x in input().split()]

print("Maxwise Product Slow ", MaxWiseProductSlow(a))
print("Maxwise Product Fast ", MaxWiseProductFast(a))

#Stress test is done wrong here. I am not doing the stress test in for loop. Instead just running the while loop
#with out any condition. This is the reason, program dint validate properly while doing stress test. It was caught
#while submitting the program to coursera
randomoutputlist = MaxWiseProductStressTest()
print(randomoutputlist)
fastresult = MaxWiseProductFast(randomoutputlist)
slowresult = MaxWiseProductSlow(randomoutputlist)


rightresultfound = 1
while rightresultfound:
    if fastresult == slowresult:
        print("OK")
    else:
        print("Wrong result", fastresult, slowresult)
        rightresultfound = 0


