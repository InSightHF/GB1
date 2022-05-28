from sys import argv
from functools import reduce
from itertools import count, cycle
from math import factorial

"""Практическая работа по Теме 4 'Импорт, модули и ...'"""

"""Задание 4.1."""

print('\n4.1.Реализовать скрипт, в котором должна быть предусмотрена функция расчёта\n'
      'заработной платы сотрудника. Использовать в нём формулу: (выработка в часах\n'
      '* ставка в час) + премия. Во время выполнения расчёта для конкретных значений\n'
      'необходимо запускать скрипт с параметрами.')
print('-' * 77)

print('Исходные данные (параметры):')
x, y, z = map(float, argv[1:])
print('Количество отработанных сотрудником часов:', x)
print('Ставка одного часа работы, в руб.:', y)
print('Размер премии, в руб.:', z)
print('\t', '.' * 30)


def income():
    pay = x * y
    return pay + z


print(f'Таким образом, размер заработной платы сотрудника составил: '
      f'{income():.2f} рублей.')

print('*' * 77)


"""Задание 4.2."""

print('\n4.2.Представлен список чисел. Необходимо вывести элементы исходного списка,\n'
      'значения которых больше предыдущего элемента. Подсказка: элементы,\n'
      'удовлетворяющие условию, оформить в виде списка. Для его формирования\n'
      'использовать генератор.')
print('-' * 77)

initial_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print('Имеем исходный список:\n\t', initial_list)
print('\t', '.' * 30)
new_list1 = [a for i, a in enumerate(initial_list) if i > 0 and initial_list[i] > initial_list[i - 1]]
print('Вариант №1 преобразования исходного списка в новый:\nРезультат переработки:\n\t', new_list1)
new_list2 = [i for i, a in zip(initial_list[1:], initial_list[:-1]) if i > a]
print('Вариант №2 преобразования исходного списка в новый:\nРезультат переработки:\n\t', new_list2)

print('*' * 70)


"""Задание 4.3."""

print('\n4.3.Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.\n'
      'Решите задание в одну строку. Подсказка: используйте функцию range()\n'
      'и генератор.')
print('-' * 70)

result = [x for x in range(20, 240) if (x % 20 == 0) or (x % 21 == 0)]
print('Полученный результат:\n', result)

print('*' * 103)


"""Задание 4.4."""

print('\n4.4.Представлен список чисел. Определить элементы списка, не имеющие повторений.\n'
      'Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести\n'
      'в порядке их следования в исходном списке. Для выполнения задания обязательно\n'
      'использовать генератор.')
print('-' * 80)

initial_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print('Имеем исходный список:\n\t', initial_list)
print('\t', '.' * 30)
new_list = [d for d in initial_list if initial_list.count(d) == 1]
print('Сформирован итоговый массив чисел, соответствующих заданию:\n\t', new_list)

print('*' * 80)


"""Задание 4.5."""

print('\n4.5.Реализовать формирование списка, используя функцию range() и возможности\n'
      'генератора. В список должны войти чётные числа от 100 до 1000 (включая границы).\n'
      'Нужно получить результат вычисления произведения всех элементов списка.\n'
      'Подсказка: использовать функцию reduce().')
print('-' * 80)

my_list = [b for b in range(100, 1001) if b % 2 == 0]
print('Сформирован список чётных чисел в заданном диапазоне:\n', my_list)
print('Результат произведение всех элементов сформированного списка:\n',
      reduce(lambda x, y: x * y, my_list))

print('*' * 80)


"""Задание 4.6."""

print('\n4.6.Реализовать два небольших скрипта:\n'
      'а) итератор, генерирующий целые числа, начиная с "x", при достижении числа\n'
      '"x + 10" — завершает цикл;\n'
      'б) итератор, повторяющий элементы некоторого списка, определённого заранее,\n'
      'при достижении 10 итераций, повторение элементов списка прекратится.\n'
      'Подсказка: используйте функцию count() и cycle() модуля itertools.\n'
      'Обратите внимание, что создаваемый цикл не должен быть бесконечным.')
print('-' * 75)

print('а) Первый скрипт:')
x = int(input('Введите целое число начала отсчёт:\n\tx = '))
print('Результат работы первого генератора c шагом 2.5:')
for element in count(x, 2.5):
    print('\t', element, end='')
    if element > (x + 10):
        break
print('\n', '-' * 75)

print('б) Второй скрипт:')
list1 = [55, 'zero', 12, 23.33, -16]
print('Имеем исходный список:\n\t', list1)
print('Результат работы второго генератора:')
iteration = 0
for series in cycle(list1):
    print('\t', series, end='')
    iteration += 1
    if iteration > 10:
        break

print('\n', '*' * 75)


"""Задание 4.7."""

print('\n4.7.Реализовать генератор с помощью функции с ключевым словом yield,\n'
      'создающим очередное значение. При вызове функции должен создаваться\n'
      'объект-генератор. Функция вызывается следующим образом: for el in fact(n).\n'
      'Она отвечает за получение факториала числа. В цикле нужно выводить только\n'
      'первые n чисел, начиная с 1! и до n!. Подсказка: факториал числа n —\n'
      'произведение чисел от 1 до n.\n'
      'Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.')
print('-' * 75)

while True:
    n = input('Введите целое положительное число количества желаемых результатов:\n\tn = ')
    try:
        n = int(n)
        if n <= 0:
            print('Вы ввели отрицалельное число или ноль. Осуществите запрашиваемый ввод.')
            print('\t', '.' * 30)
            continue
        else:
            print('Программа уже посчитала факториал каждого из', n, 'чисел!!!')
            break
    except ValueError:
        print('Вы ввели некорректные данные. Попробуйте новый ввод.')
        print('\t', '.' * 30)


def factor_gen(n):
    for i in range(1, n + 1):
        print(i, end='! = ')
        yield factorial(i)


print('Вот результаты:')
for element in factor_gen(n):
    print(element)

print('*' * 75)
print('END')
