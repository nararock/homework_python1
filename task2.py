seconds = int(input('Введите количество секунд: '))

hours = seconds // 3600
seconds -= hours * 3600
minutes = seconds // 60
seconds -= minutes * 60

print(f'{hours}:{minutes}:{seconds}')




