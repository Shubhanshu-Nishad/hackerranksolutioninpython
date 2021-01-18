# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = input().split()


storage = list()
count = 0

storage = list(map(int, input().strip().split()))

A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))

for i in storage:
    if i in A:
        count = count+1
    if i in B:
        count = count-1

print(count)
