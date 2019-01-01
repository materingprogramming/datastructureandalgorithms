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

n = int(input())

a = [int(x) for x in input().split()]

print(MaxWiseProductFast(a))

