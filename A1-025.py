
card = {"K":"king","J":"jack","Q":"queen","S":"spades","C":"clubs","D":"diamonds","H":"hearts","A":"ace","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":'8',"9":"9","10":"10"}
c = input()
c = c.upper()
c1 = c[0:-1]
c2 = c[len(c)-1]
print(f"{card[c1]} of {card[c2]}")
