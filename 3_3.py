lst = [10, 17, 13, 44, 23, 88, 100, 99]
print('Напечатаем-ка только четные числа:')
for i in lst:
    if i % 2 == 0:
        print(i)

print('А теперь - только нечетные числа:')

for i in lst:
    if i % 2 != 0:
        print(i)
