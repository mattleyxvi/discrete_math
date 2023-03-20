import math
c=int(input())
a=[[] for i in range(c)]
for i in range(c):
    for j in range(c):
        a[i].append(int(input()))
        if a[i][j]==-1:
            a[i][j]=math.inf
for k in range(c):
    for i in range(c):
        for j in range(c):
            if i!=j :
                a[i][j]=min(a[i][k]+a[k][j],a[i][j])
for i in a:
    print(i)
