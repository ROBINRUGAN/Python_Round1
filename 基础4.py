mew = []
while True:
    x = input()
    try:
        x = int(x)
    except:
        pass
    if x != '':
        mew.append(x)
    else:
        break

for qwq in mew:
    if type(qwq) == str:
        mew.remove(qwq)
mew.sort()
print(*mew)
