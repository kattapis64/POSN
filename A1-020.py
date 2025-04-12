
a=int(input())
b=int(input())
c=int(input())
l = [a,b,c]
min=0
max=0
for i in range(len(l)):
    if l[i] == l[0]:
        continue
    elif l[i] < l[i-1]:
        min+=1

    elif l[i] > l[i-1]:
        max+=1
if min == 2:
    print("decreasing")
elif max==2:
    print("increasing")
else:
    print("neither")

