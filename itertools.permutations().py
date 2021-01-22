# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
n=list(map(str,input().split()))
a=n[0]
b=int(n[1])
# ls = list(permutations(a,b))
#ls = list(permutations("shub",2))
for i in sorted(permutations(n[0], int(n[1]))):
    print(''.join(i))
