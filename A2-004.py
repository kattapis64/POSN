n = int(input())
x={}
for i in range(n):
    k = input()
    if k in x:
        x[k]+=1
    else:
        x[k]=1
print(max(x.values()))