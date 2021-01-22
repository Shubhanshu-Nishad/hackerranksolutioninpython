# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
n=list(map(str,input().split()))
k=int(n[1])
for i in range(1,k+1):
    for j in combinations(sorted(n[0]),i):
        print("".join(j))
