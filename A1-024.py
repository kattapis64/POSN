y = int(input())
cc =int(input())
if y<=1990:
    if cc <=1500:
        print(1250)
    elif cc > 1500 and cc<=2000:
        print(1400)
    elif cc>2000:
        print(2000)
elif y <= 1999 and y >=1991:
    if cc <=1500:
        print(1100)
    elif cc > 1500 and cc<=2000:
        print(1300)
    elif cc>2000:
        print(1700)
elif y>=2000:
    if cc <=1500:
        print(1000)
    elif cc > 1500 and cc<=2000:
        print(1200)
    elif cc>2000:
        print(1500)
