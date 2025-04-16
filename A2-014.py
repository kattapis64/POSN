global k

n= input().lower()
m=input().lower()
if len(n)>len(m):
    m= m+m[0:len(n)-len(m)]
else:
    n = n + n[0:len(m) - len(n)]
m=list(m.strip(""))
n=list(n.strip(""))
a=[]
countn = sum([n.count("l"),n.count("o"),n.count("v"),n.count("e")])
countm = sum([m.count("l"),m.count("o"),m.count("v"),m.count("e")])
for i,j in zip(m,n):
    if i=="l" or i =="o" or i =="v" or i== "e":
        a.append("w")
    elif j=="l" or j =="o" or j =="v" or j== "e":
        a.append("w")
    else:
        a.append("$")
k = a.count("w")
if k%2 == 0:
    a= "".join(a)
    if "ww" in a:
        print(a)
    else:
        print(a+"#")
else:
    e = len(sorted("".join(a).split("$"))[len(sorted("".join(a).split("$")))-1:][0])
    print("".join(a) + str(e))


