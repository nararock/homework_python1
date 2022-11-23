revenue = float(input('Введите значение выручки: '))
charge = float(input('Введите значение издержек: '))
amount_employees = int(input('Введите количество сотрудников: '))
profit = revenue - charge

if profit > 0:
    print('Финансовый результат: прибыль.')
    print(f'Рентабельность равна {round(profit / revenue, 2)}')
    print(f'Прибыль на 1 сотрудника: {round(profit / amount_employees, 2)}')
else:
    print('Финансовый результат: убыток.')
