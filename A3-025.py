
logs = [[1,1,0,1,1,1,1,0],
        [1,1,1,0,0,1,1,1],
        [1,0,1,1,0,0,1,1],
        [1,0,1,1,0,0,1,1]]
limit = [3,8,1]
zero1 = []
for k in range(0,limit[0]):
        for i in range(8):
                if logs[k][i] == 0:
                        zero1.append(str(i))
                        zero1.append(" ")

        zero1.append("s")
stri = ("".join(zero1)).split("s")[0:limit[0]]
print(stri)
stri1 = []
for i in range(1,4):
        stri1.append(stri[i-1].split(" ")[0:-1])
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
for k in range(limit[0]):
        res.append(tab*k)
        res.append(f"for {alp[k]} in range(len(stri1[0])):\n")
for j in range(limit[0]-1):
        res.append(tab*(j+3))
        res.append(f"if (int(stri1[0][{alp[j]}]) == (int(stri1[1][{alp[j+1]}]))+1) or (int(stri1[0][{alp[j]}]) == (int(stri1[1][{alp[j+1]}]))-1):\n")
res.append(tab*((2*limit[0])-1))

res.append("mu +=1\n")




print(res)
res = "".join(res)
print(res)
exec(res)

if mu ==1:
        print("yes")
else:
        print("no")







