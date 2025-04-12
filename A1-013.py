letter = input()
pw = input()
if letter =="H":
    if pw == "4567":
        print("safe unlocked")

    elif pw != "4567":
        print("safe locked - change digit")
elif letter != "H":
    if pw == "4567":
        print("safe locked - change char")

    elif pw != "4567":
        print("safe locked")