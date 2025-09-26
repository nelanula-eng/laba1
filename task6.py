s = input("Введите строку: ").lower()
vowels = "аеёиоуыэюяaeiou"
count = sum(1 for ch in s if ch in vowels)
print(f"Количество гласных: {count}")
