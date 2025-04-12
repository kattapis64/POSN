roman = ["I","II","III","IV","V","VI","VII","VIII","IX","I"]
j = int(input())
if j <=9 and j>=1:
    print(roman[j-1])
elif j < 0:
    print("Error : Please input positive number")
else:

    print("Error : Out of range")