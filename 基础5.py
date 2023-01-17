mewctionary = {'222200314': 'mewww', '222200315': '俊腾giegie', '052106112': '小黄老师'}
a = []
for key, value in mewctionary.items():
    if int(key) % 2 == 0:
        a.append(key)
for i in a:
    del mewctionary[i]
print(mewctionary)
