def countAfter(x,u,l):
    a = l.split(x)
    h=[]
    for i in a:
        h.append(i.count(u))
    return max(h)
def firstIndex(g,i):
    for j in i:
        if j ==g:
            return i.index(j)
global c
nat = "BUUBUUBUUBUU"
o = input()
s=o.lower()
if "buu" in s:
    print("Yes",(countAfter("b","u",s)))

elif "b" in o:
    o = list(o.strip())
    ind = firstIndex("b",o)
    lef = len(o)-ind-1
    print("".join(o[0:ind+1]) + "U"*lef)
elif "B" in o:
    o = list(o.strip())
    ind = firstIndex("B", o)
    lef = len(o) - ind - 1
    print("".join(o[0:ind + 1]) + "U" * lef)
else:
    print(nat[:len(s)])