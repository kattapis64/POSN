n = int(input())
vowel = ["A","E","I","O","U"]
k=0
for i in range(n):
    x=input()
    for j in x:
        if j in vowel:
            k+=1
print(k)
