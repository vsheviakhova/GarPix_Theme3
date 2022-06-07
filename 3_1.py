counter = 0
n = int(input('Сколько чисел вы хотите ввести? '))
for i in range(1, n+1):
    number = int(input('Введите число: '))
    if number % 2 == 0:
        counter += 1
print(f'Всего четных чисел: {counter}')

