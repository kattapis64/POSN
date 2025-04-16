s=input()
n,q = map(int,s.split(" "))
D=[]
L=[]
for i in range(n):
    h = input()
    d,l = map(int,h.split(" "))
    D.append(d)
    L.append(l)
print(D,"\n",L)
hi = 0
k =[]
for i in D:
    hi += i
    k.append(shi)
print(k)
j=[]
for f in L:
    j.append((k[L.index(f)],f))
print(j)
print(sorted(j))