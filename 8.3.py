def min_boats_to_transport(m, n, weights):
    # Сначала сортируем веса рыбаков по возрастанию
    weights.sort()

    # Инициализируем переменные
    boats = 0
    left = 0  # Индекс самого легкого рыбака, оставшегося на берегу
    right = n - 1  # Индекс самого тяжелого рыбака, оставшегося на берегу

    while left <= right:
        # Если самый тяжелый рыбак не может поместиться в лодке, то он остается на берегу
        if weights[right] > m:
            right -= 1
        else:
            # Если самый тяжелый рыбак может поместиться с самым легким в лодке
            if weights[right] + weights[left] <= m:
                left += 1
            right -= 1  # Перевозим самого тяжелого рыбака
            boats += 1

    return boats, n - boats  # Возвращаем количество переплывших и оставшихся на берегу

# Ввод данных
m = int(input("Введите максимальную массу, которую может выдержать одна лодка: "))
n = int(input("Введите количество рыбаков: "))

weights = []
for i in range(n):
    weight = int(input(f"Введите вес моряка {i + 1}: "))
    weights.append(weight)

# Вызываем функцию и выводим результат
result, remaining = min_boats_to_transport(m, n, weights)
print(f"Минимальное количество лодок, необходимое для переправки всех рыбаков: {result}")
if remaining > 0:
    print(f"Моряков переплыло: {result}, Моряков осталось на берегу: {remaining}")
