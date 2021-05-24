rows = int(input("write num of rows :"))
count = 0
count2 = rows
gg = False
for i in range(0, rows):
    if i == int(rows / 2) + 1:
        print(' ' * (int(rows / 2)) + '*' * rows)
        count = rows - 1
        count2 = int(count / 2) + 1
        gg = True
    for j in range(0, count):
        if j == 0:
            print(' ' * count2, end='')
        else:
            print('*', end="")
    print()
    if not gg:
        count += 2
        count2 -= 1
    else:
        count -= 2
        count2 += 1