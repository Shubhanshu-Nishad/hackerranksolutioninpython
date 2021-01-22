import itertools
k,m = map(int, input().split())
l = []
for i in range(k):
  l.append([x*x for x in list(map(int, input().split()))[1:]])
 
s = 0
for e in itertools.product(*l):
  temp = sum(e)%m
  if temp > s:
    s = temp
print(s)
