N = int(input("Введите число N: "))
fact = 1
for i in range(1, N + 1):
    fact *= i
print(f"Факториал числа {N} равен {fact}")
