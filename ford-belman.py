import math
a=int(input())
k=0
l=[[0 for i in range(a)] for j in range(a)]
c=[[0 for i in range(a)] for j in range(a)]
for i in range(a):
    b=input().split(' ')
    for j in range(len(b)):
        try:
            c[i][j]=int(b[j])
        except (ValueError):
            c[i][j]=math.inf
for i in range(a):
    l[0][i]=math.inf

l[0][0]=0
    
for k in range(1,a):
    l[k][0]=0
    for i in range(1,a):
        
        l[k][i]=min(l[k-1][0]+c[0][i],l[k-1][1]+c[1][i])
        for j in range(2,a):
            l[k][i]=min(l[k][i],l[k-1][j]+c[j][i])
    print(l)
for i in (l):
    print(i)
#5
#inf 1 inf inf 3
#inf inf 8 7 1
#int i i 1 -5
#i i 2 i i
#i i i 4 i
