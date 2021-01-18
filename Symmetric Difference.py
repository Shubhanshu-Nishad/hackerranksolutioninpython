# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
set1 = set(map(int,input().split()))
n=int(input())
set2 = set(map(int,input().split()))
set3=set1.symmetric_difference(set2)
ls = list(set3)
ls.sort()
for i in ls:
    print(i)
