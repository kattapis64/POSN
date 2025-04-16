next = {"Red":"Green","Green":"Blue","Blue":"Red"}
color = {"R":"Red","G":"Green","B":"Blue"}
a,b = map(str,input().split())
b= int(b)
ans=[color[a]]
for i in range(b-1):
    ans.append(next[ans[i]])
print(" ".join(ans))