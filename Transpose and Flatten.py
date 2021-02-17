import numpy
import numpy
n, m = map(int, input().split())

s = numpy.array([input().strip().split() for i in range(n)], int)
print (s.transpose())
print (s.flatten())
