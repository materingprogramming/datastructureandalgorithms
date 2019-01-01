#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    for i in range(0, len(a)):
        print(a[i])


if __name__ == '__main__':
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

#   fptr.write(' '.join(map(str, res)))
  #  fptr.write('\n')

   # fptr.close()