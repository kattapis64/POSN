vowel = ["a","e","i","o","u"]
n=0
txt = input()
for i in txt:
    if i in vowel:
        n+=1
print(n)