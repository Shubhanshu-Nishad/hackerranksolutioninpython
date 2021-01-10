#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    w=[]
    ar=0
    br=0
    for i in range(len(a)):
        if a[i]>b[i]:
            ar += 1
        if a[i]<b[i]:
            br +=1
    w.append(ar)
    w.append(br)
    return w
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
