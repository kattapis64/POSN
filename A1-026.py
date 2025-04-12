a,b,c = int(input()),int(input()),int(input())
l = [a,b,c]
odd=0
even = 0
for i in l:
    if i %2 ==0:
        even +=1
    elif i%2 ==1:
        odd +=1
print(f"even {even}\nodd {odd}")
