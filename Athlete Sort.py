import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][k] > arr[j+1][k]:
                arr[j] , arr[j+1]=  arr[j+1] ,arr[j]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j],end=" ")
        print()

