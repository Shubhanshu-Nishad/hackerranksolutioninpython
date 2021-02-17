import numpy
n, m ,p= map(int, input().split())

s = numpy.array([input().strip().split() for i in range(n+m)], int)
print(s)
