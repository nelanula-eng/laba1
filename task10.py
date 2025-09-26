arr = list(map(int, input("Введите массив чисел через пробел: ").split()))
X = int(input("Введите число для поиска: "))
if X in arr:
    print(f"Число {X} содержится в массиве")
else:
    print(f"Число {X} не найдено в массиве")
