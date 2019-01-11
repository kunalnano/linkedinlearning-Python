a, b = 0, 1
while b < 2000:
    print(b, end= ' ', flush = True)
    a, b = a, a+b
print()
