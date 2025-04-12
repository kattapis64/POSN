limit = input()
limit = limit.split(" ")
rho = []
for o in range(int(limit[0])):
     r = input()[2:].split(" ")
     rho.append(r)
print(rho)
for q in rho:
    for p in q:
        print(p)
        q[q.index(p)] = int(p)-1
print(rho)
stri1 = rho

