n = int(input("Введите число N: "))

numbers = []
for i in range(n):
    num = int(input())
    numbers.append(num)

reversed_numbers = numbers[::-1]

print(*reversed_numbers)
