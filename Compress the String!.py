# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *

string = input()
for i,j in groupby(map(int,list(string))):
    print(tuple([len(list(j)), i]) ,end = " "
