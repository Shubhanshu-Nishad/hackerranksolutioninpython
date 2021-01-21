# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m =input().split()
n=int(n)
m=int(m)
g=''
h='.|.'
x=""
for i in range(int(n/2)):
    g +=h
    x = g.center(m, "-")
    print(x)
    g +=h
c="WELCOME"
cen=c.center(m,"-")
print(cen)
for i in range(n-2,-1,-2): 
    print((i * ".|.").center(m, "-"))
