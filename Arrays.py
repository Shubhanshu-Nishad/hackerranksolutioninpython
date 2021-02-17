import numpy

def arrays(arr):
    return(numpy.array(arr[::-1], float))
    return arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
