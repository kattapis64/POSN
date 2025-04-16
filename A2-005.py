a = input()
w,h,m,n = map(int,a.split(' '))

b = input()
x= list(map(int,b.split(" ")))
c = input()
y= list(map(int,c.split(" ")))

x.append(w)
y.append(h)
x.insert(0,0)
y.insert(0,0)
xt =[]
yt=[]
for i in range(1,len(x)):
    xt.append(x[i]-x[i-1])
for i in range(1,len(y)):
    yt.append(y[i]-y[i-1])

xt = sorted(xt)[::-1][0:2]
yt = sorted(yt)[::-1][0:2]

ans = sorted([xt[0]*yt[1],xt[0]*yt[0],yt[0]*xt[1],xt[1]*yt[0]])[::-1]
print(ans[0],ans[1])