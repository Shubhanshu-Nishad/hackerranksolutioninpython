# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
n=list(map(str,input().split()))
for i in combinations_with_replacement(sorted(n[0]), int(n[1])):
    print(''.join(i))
