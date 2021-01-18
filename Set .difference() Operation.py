# Enter your code here. Read input from STDIN. Print output to STDOUT
ne = int(input())
setne = set(map(int,input().split()))
nf = int(input())
setnf = set(map(int,input().split()))
set3 = setne.difference(setnf)
print(len(set3))
