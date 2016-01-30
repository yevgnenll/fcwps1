rabbits = ['flopy', 'mopsy', 'cotton', 'peter']
cur = 0
while cur < len(rabbits):
    print(rabbits[cur])
    cur += 1

else:
    if cur == 1:
        print("i have 1 rabbit")
    else:
        print("i have", cur, "rabbits")

count = 0
sat = 2
while count <= 100:
    if count % 2 == 0:
        print(count)
    count += 1

    if sat*48 > count:
        break
else:
    print("current count is", count)