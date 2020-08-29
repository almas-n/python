
#Задание1
a = 1
b = 2.2
c = 'Almaty'
print(a, b, c)
a = int(input("Введите целое число: "))
b = float(input("Введите дробное число: "))
c = (input("Введите слово: "))
print(a, b, c)

#Задание2
a = int(input("Введите количество секунд: "))
if a >= 60:
    b = a // 60
    a = a % 60
    if b >= 60:
        c = b // 60
        b = b % 60
# print('{2}:{1}:{0}'.format(a, b, c))
print(f"{c}:{b}:{a}")

#Задание3
n = int(input('Введите число n: '))
nn = n * 11
nnn = n * 111
a = n + nn + nnn
print(a)

#Задание4

num = int(input('Введите целое число: '))
max = 0
a=0
while num>max:
    a = num % 10
    if max < a:
        max = a
    if max == 9:
        break
    num //= 10
    if num == 0:
        break
print(max)

#Задание5
vyr = int(input('Введите значение выручки: '))
izd = int(input('Введите значение издержки: '))
if vyr > izd:
    print('Ваша компания получает прибыль')
    rentab = vyr / izd * 100
    print(f'Рентабельность компании: {rentab} %')
    sotr = int(input('Введите количество сотнудников: '))
    pribyl = ( vyr - izd )/sotr
    print(f'Прибыль фирмы в расчете на одного сотрудника составляет: {pribyl} руб.')
else:
    print('Ваша компания несёт убытки')

#Задание6
a = int(input('Резульат в первый день: '))
b = int(input('Желаемый результат: '))
day = 0
while a < b:
    day += 1
    print(f'{day}-й день: {a} ') #так и не понял как округлить при использовании f-строк
    a += a * 0.1
    if b < a:
        day += 1
        print(f'{day}-й день: {a} ')
        a += a * 0.1
        break
