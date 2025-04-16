n=int(input())
s = list(map(int,input().split(" ")))
temp=s
res=0
if n==1:
    print(1)
else:
    for i in range(len(temp)):
        try:
            if temp[i]>temp[i+1] and temp[i]>temp[i-1]:
                res+=1
        except IndexError:
            if i ==len(temp)-1 and temp[i]>temp[i-1]:
                res+=1
            elif i ==0 and temp[i]>temp[i+1] :
                res+=1

    print(res) 