n = int(input("Введите число N: "))

numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)

new_numbers = []
for i in range(-1,len(numbers)-1):
    new_numbers.append(numbers[i])

print(*new_numbers)
