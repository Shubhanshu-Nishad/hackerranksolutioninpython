n=int(input())
ls=list(map(int,input().split()))
cust = int(input())

cost=0
shoe=[]
for i in range(cust):
    s=list(map(int,input().split()))
    if s[0] in ls:
        cost +=s[1]
        ls.remove(s[0])
print(cost)
