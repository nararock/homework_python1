num = int(input('Введите число: '))
max_num = 0
while num != 0:
    temp = num % 10
    num //= 10
    if temp > max_num:
        max_num = temp

print(f"Максимальная цифра: {max_num}")
