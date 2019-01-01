#Uses python3
import array

def InsertionSortNotDecreasing(inputs):
    for i in range(1, len(inputs)):
        key = inputs[i]
        j = i - 1
        while (j >= 0 and inputs[j] > key):
            inputs[j + 1] = inputs[j]
            j = j -1
        inputs[j + 1] = key
    return inputs

def InsertionSortNotIncreasing(inputs):
    for i in range(1, len(inputs)):
        key = inputs[i]
        j = i - 1
        while (j >= 0 and inputs[j] < key):
            inputs[j + 1] = inputs[j]
            j = j -1
        inputs[j + 1] = key
    return inputs


inputs = [20, 45, 98, 18, 57, 92, 1, 74, 5, 45]
outputs = InsertionSortNotDecreasing(inputs)
for x in outputs:
    print(x)

print("---------------------------------------------")

nonincreasingoutputs =InsertionSortNotIncreasing(inputs)
for x in nonincreasingoutputs:
    print(x)
