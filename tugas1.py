def perkalian(a, b):
    hasil = 0
    for x in range(a):
        hasil += b
    return hasil

x = 6
y = 5
print(f"{x} x {y} =", end=" ")

for i in range(x):
    if i == x - 1:
        print(y, end=" ")
    else:
        print(y, "+", end=" ")

print("=", perkalian(x, y))

x = 7
y = 10
print(f"{x} x {y} =", end=" ")

for i in range(x):
    if i == x - 1:
        print(y, end=" ")
    else:
        print(y, "+", end=" ")

print("=", perkalian(x, y))
