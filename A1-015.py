name = input()
sur = input()
age = input()
if( len(name) > 5) and (len(sur) > 5):
    print(f"{name[0:2]}{sur[len(sur) - 1]}{age[len(age) - 1]}")
else:
    print(f"{name[0]}{age}{sur[len(sur) - 1]}")
