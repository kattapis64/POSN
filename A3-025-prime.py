l = input()
l = l.split(" ")

limit=[]
for w in range(3):
        limit.append(int(l[w]))
rho = []
for o in range(int(limit[0])):
     r = input()[2:].split(" ")
     rho.append(r)
print(rho)
for q in rho:
    for p in q:
        print(p)
        q[q.index(p)] = int(p)-1
print(rho)
stri1 = rho
print(stri1)
alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
mu = 0
'''for a in range(len(stri1[0])):
        for b in range(len([stri1[1]])):
                for c in range(len([stri1[2]])):
                        if (int(stri1[0][a]) == (int(stri1[1][b]))+1) or (int(stri1[0][a]) == (int(stri1[1][b]))-1):
                                if (int(stri1[0][b]) == (int(stri1[1][c])) + 1) or (int(stri1[0][b]) == (int(stri1[1][c])) - 1):
                                        print("yes")'''
tab = "    "
res=[]
res.append("for y in range(0,limit[2]):\n")

for k in range(limit[0]):
        res.append(tab*(k+1))
        res.append(f"for {alp[k]} in range(len(stri1[0])):\n")
for j in range(limit[0]-1):
        res.append(tab*(j+limit[0]+1))
        res.append(f"if (int(stri1[0][{alp[j]}]) == (int(stri1[1][{alp[j+1]}]))+y+1) or (int(stri1[0][{alp[j]}]) == (int(stri1[1][{alp[j+1]}]))-y-1):\n")
res.append(tab*((2*limit[0])))

res.append("mu +=1\n")




print(res)
res = "".join(res)
print(res)
exec(res)

if mu ==1:
        print("yes")
else:
        print("no")







