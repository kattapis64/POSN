y = int(input())
def isLeap(y):
    if y%4==0:
        if y < 1582:
            return "yes"
        else:
            if y%400 == 0:
                return "yes"
            elif y%100 == 0:
                return "no"
            else:
                return "yes"
    else:
        return "no"
print(isLeap(y))