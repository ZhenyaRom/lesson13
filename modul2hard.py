x = int(input('Введите число от 3 до 20: '))
parol = []
for i in range(1, x):
    for j in range(i + 1, x):
        if (x % (i + j)) == 0:
            parol.append([i, j])
print(parol)

