#Кошовий Давид
size = int(input())

for line in range(size):
    for number in range(line + 1, 0, -1):
        print(number, end= ' ')
    print()