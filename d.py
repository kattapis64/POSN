txt = input().upper()

counts = {}
order = []

for ch in txt:
    if ch.isalpha():
        if ch not in counts:
            counts[ch] = 1
            order.append(ch)
        else:
            counts[ch] += 1

ans = ""
for ch in order:
    ans += f"{counts[ch]}{ch}"

print(ans)
