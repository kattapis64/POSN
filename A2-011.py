s = input()
s = list(map(str,s.split(" ")))
count={}
for i in s:
    if i in count:
        count[i] +=1
    else:
        count[i]=1
print(" ".join(list(count.keys())))