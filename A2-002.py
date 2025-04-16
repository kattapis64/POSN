n= int(input())
c=[]
for i in range(n):
    p = str(input())
    s = p.split(' ')
    c.append(s)
def canTent(x,y,q,r):
    if (x - q) == 0 and y - r == 0:
        return 0

    elif (x-q)**2 == (y-r)**2:
        return abs(x-q)
    else:
        return 0
m=0
for j in c:
    for k in c:
        h = (canTent(int(j[0]),int(j[1]),int(k[0]),int(k[1])))
        if h=="0" or h==0:
            continue
        else:
            if h>m:m=h
print(m)
