n = int(input())
s = input()
s=s.split(" ")
l=[]
for i in range(0,n*2-1,2):
    if int(s[i])>int(s[i+1]):
        l.append(int(s[i]))

    elif int(s[i+1])>int(s[i]):
        l.append(int(s[i+1]))
    else:
        l.append(int(s[i]))

ans=[]
ans.append(str(l[0]))
sum =0
for j in l:
    sum+=int(j)
if len(l) == 1:
    print(l[0])
else:

    for i in l[1:]:
        ans.append(f" + {i}")
    ans.append(f" = {sum}")
    print("".join(ans))