x = int(input())
for i in range(x):
    numbers = [str(i + 1) for j in range(x - i)]
    print(' '.join(numbers))