# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input())
array = input().split()
k = int(input())

comb_ls = list(combinations(array, k))
a_ls = [e for e in comb_ls if 'a' in e]
print(len(a_ls) / len(comb_ls))
