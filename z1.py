a = input('Введите число: ')

def sum(a):                            
    if float(a) < 0:                            
        a = float(a) * (-1)
    num = 0

    for i in str(a):
        if i != '.':
            num += int(i)
    return num

print(f'Сумма чисел равна {sum(a)}')