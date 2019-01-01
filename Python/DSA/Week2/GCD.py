#Uses python3

def GCDFast(firstnumber, secondnumber):

    if secondnumber == 0:
        return firstnumber
    else:
        reminder = firstnumber % secondnumber
    return GCDFast(secondnumber, reminder)

a = [int(x) for x in input().split()]

result = GCDFast(a[0], a[1])

print(result)



