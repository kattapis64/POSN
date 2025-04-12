txt = input()
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
k=0
l=0
m=0
n=0
o=0
p=0
q=0
r=0
s=0
t=0
u=0
v=0
w=0
x=0
y=0
z=0
txt = txt.lower()
for gr in txt:
    exec(f"{gr}+=1")
sv ={}
sv['a'] = a
sv['b'] = b
sv['c'] = c
sv['d'] = d
sv['e'] = e
sv['f'] = f
sv['g'] = g
sv['h'] = h
sv['i'] = i
sv['j'] = j
sv['k'] = k
sv['l'] = l
sv['m'] = m
sv['n'] = n
sv['o'] = o
sv['p'] = p
sv['q'] = q
sv['r'] = r
sv['s'] = s
sv['t'] = t
sv['u'] = u
sv['v'] = v
sv['w'] = w
sv['x'] = x
sv['y'] = y
sv['z'] = z


svn = {nb: gd for nb, gd in sv.items() if (gd != 0 and isinstance(gd, int) == True)}
gh = list(svn.values())

gn = list(svn.keys())

ans=[]
for xc in range(0,((len(gh)*2))):

    if xc %2 == 1:

        ans.append(str(gn[int(xc/2)]))
    elif xc %2 ==0:

        ans.append(str(gh[int(xc/2)]))


ans = "".join(ans)
ans = ans.upper()
print(ans)

