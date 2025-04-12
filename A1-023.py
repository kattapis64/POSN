t = int(input())
u = input()
u = u.lower()

if u=="f":
    t= (t-32)/9
if t <= 0:
    print("solid")
elif t> 0 and t<100:
    print("liquid")
elif t >= 100:
    print("gas")