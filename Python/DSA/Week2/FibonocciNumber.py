#Uses python3
import array

def CalculateFibonocciNumber(input):
    fibseries = [0] * input

    fibseries[0] = 0
    fibseries[1] = 1

    for i in range(input):
        if i > 1:
            fibseries[i] = fibseries[i - 1] + fibseries[i - 2]


    return fibseries[input-1]

n = int(input())

if n <= 1:
    result = n
else:
    result = CalculateFibonocciNumber(n)

print(result)



