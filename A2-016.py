s, n = input().split()
b, a = input().split()

if s == b and n == a:
    print(1000000)
elif n == a:
    print(100000)
elif n[-3:] == a[-3:] and s == b:
    print(2000)
elif n[-3:] == a[-3:]:
    print(200)
elif n[-2:] == a[-2:] and s == b:
    print(1000)
elif n[-2:] == a[-2:]:
    print(100)
elif s == b:
    print(20)
else:
    print(0)
#HELLo
