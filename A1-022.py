next = [19,18,20,19,20,21,22,22,22,23,21,21]
mo = ["capricorn","aquarius","pisces","aries","taurus","gemini","cancer","leo","virgo","libra","scorpio","sagittarius"]
d = int(input())
m = int(input())


if d > next[m-1]:
    if m == 12:
        m=0
    print(mo[m])
else:
    print(mo[m-1])