a= list(str(input())[::-1])
for i in range(len(a)//3):
    a.insert(((i+1)*4)-1,",")
s = a[::-1]
if s[0] == ",":
    s.pop(0)
print("".join(s))