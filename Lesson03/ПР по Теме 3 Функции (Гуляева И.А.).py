
"""Практическая работа по Теме 3 'Функции'"""

"""Задание 3.1."""

print('\n3.1.Реализовать функцию, принимающую два числа (позиционные аргументы) и\n'
      'выполняющую их деление. Числа запрашивать у пользователя, предусмотреть\n'
      'обработку ситуации деления на ноль.')
print('-' * 75)

print('Программа подсчёта частного:')


def division(x, y):
    try:
        x / y
    except ZeroDivisionError:
        print('\t', '.' * 30)
        print('Не стоит искушать судьбу - на ноль делить нельзя!')
    else:
        print('\t', '.' * 30)
        print(f'Успешный ввод! Частное введённых чисел равно: {x / y:.2f}')
    return


division(float(input('Введите первое число (делимое):\n\tx = ')),
         float(input('Введите второе число (делитель):\n\ty = ')))

print('*' * 75)


"""Задание 3.2."""

print('\n3.2.Выполнить функцию, которая принимает несколько параметров, описывающих\n'
      'данные пользователя: имя, фамилия, год рождения, город проживания, email,\n'
      'телефон. Функция должна принимать параметры как именованные аргументы.\n'
      'Осуществить вывод данных о пользователе одной строкой.')
print('-' * 75)

print('Личная карточка пользователя:')


def user_data(name, surname, year_birth, current_city, email, phone):
    print('\t', '.' * 30)
    print(f'Проверте, правильно ли программа заполнила Ваши данные:\n'
          f'"{name} {surname} {year_birth} {current_city} {email} {phone}"')
    return


user_data(name=input('Введите своё имя: '),
          surname=input('Введите свою фамилию: '),
          year_birth=input('Введите год свого рождения: '),
          current_city=input('Введите город свого проживания: '),
          email=input('Введите свой E-mail: '),
          phone=input('Введите свой телефон: '))

print('*' * 70)


"""Задание 3.3."""

print('\n3.3.Реализовать функцию my_func(), которая принимает три позиционных\n'
      'аргумента и возвращает сумму наибольших двух аргументов.')
print('-' * 70)


def my_func(a, b, c):
    min(a, b, c)
    if min(a, b, c) == a:
        print('Функция нашла Максимумы из 3-х введённых чисел - это "b" и "c"')
        return b + c
    elif min(a, b, c) == b:
        print('Функция нашла Максимумы из 3-х введённых чисел - это "a" и "c"')
        return a + c
    elif min(a, b, c) == c:
        print('Функция нашла Максимумы из 3-х введённых чисел - это "a" и "b"')
        return a + b


try:
    x = int(input('Введите первый позиционный аргумент (целое число):\n\t"a" = '))
    y = int(input('Введите второй позиционный аргумент (целое число):\n\t"b" = '))
    z = int(input('Введите третий позиционный аргумент (целое число):\n\t"c" = '))
    print('\t', '.' * 30)
    print('Тогда сумма этих максимальных чисел равна:', my_func(x, y, z))
except ValueError:
    print('Сожалею, но Вы ввели данные не требуемого позиционного аргумента.')

print('*' * 70)


"""Задание 3.4."""

print('\n3.4.Программа принимает действительное положительное число "x" и целое\n'
      'отрицательное число "y". Выполнить возведение числа "x" в степень "y".\n'
      'Задание реализовать в виде функции my_func(x, y). При решении задания нужно\n'
      'обойтись без встроенной функции возведения числа в степень.\n'
      'Подсказка: решить задачу двумя способами. Первый — возведение в степень с\n'
      'помощью оператора **. Второй — с использованием цикла.')
print('-' * 75)

print('ПАМЯТКА! Действительными или вещественными числами называются все положительные\n'
      'числа, отрицательные числа и нуль. Действительные числа - числа, которые можно\n'
      'записать в виде конечной или бесконечной (периодической или непериодической)\n'
      'десятичной дроби.')
print('-' * 75)

print('В принципе представленные варианты функций позволяют возвести любое число\n'
      'в любую целую степень.\n'
      'Первый способ (простой):')

x = float(input('Введите основание - положительное действительное число:\n\tx = '))
y = int(input('Введите степень - отрицательное целое число:\n\ty = '))


def my_func(x, y):
    k = x ** y
    return k


print(f'Первый результат: {my_func(x, y):.10f}')
print('\t', '.' * 30)
print('Второй способ (реализация с циклом):')


def my_func(a, b):
    res = 1
    for i in range(abs(b)):
        res *= a
    if b < 0:
        return f'Второй результат: {1/res:.10f}'
    else:
        return f'Второй результат: {res:.10f}'


print(my_func(float(input('Введите основание - положительное действительное число:\n\tx = ')),
              int(input('Введите степень - отрицательное целое число:\n\ty = '))))


print('*' * 75)


"""Задание 3.5."""

print('\n3.5.Программа запрашивает у пользователя строку чисел, разделённых пробелом.\n'
      'При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить\n'
      'ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых\n'
      'чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится\n'
      'специальный символ - #, выполнение программы завершается. Если специальный\n'
      'символ введён после нескольких чисел, то вначале нужно добавить сумму этих\n'
      'чисел к полученной ранее сумме, и после этого завершить программу.')
print('-' * 80)

print('Программа подстёта суммы введённых чисел.')
print('\t', '.' * 30)

"""Для организации программы введём специальную функцию - main, в ходе выполнения которой
упорядочено вызываются вложенные в неё функции"""


def main():
    """Запустим бесконечный цикл. В нём сначала необходимо преобразовать строку с введёнными
    числами, разделенные пробелами, в список строк с числами, а затем вычислять сумму. """
    summ_0 = 0
    count = 0
    while True:
        count += 1
        print(str(count) + '-й цикл:')
        line = input('Введите строку чисел, разделённых пробелом:\n\t')
        if line == '#':
            print('Вы ввели специальный символ завершения программы.')
            break
        else:
            str_list = line.split(' ')
            print('Список строк с введёнными числами:\n\t', str_list)

        """Для преобразования списка строк с числами включая десятичные c разделением их
        по типам int и float, необходимо перед преобразованием в тип float проверять строку
        на вхождение точки '.'. А для проверки строки на целое число перед преобразованием
        проверим, что строка состоит только из десятичных чисел str.isdigit()."""
        def str_to_num(str):
             str = str.strip()
             if '.' in str and str.replace('.', '').isdigit():
                 return float(str)
             elif '-' in str and str.replace('-', '').isdigit():
                 return int(str)
             elif str.isdigit():
                 return int(str)

        num_list = []
        for i in str_list:
            n = str_to_num(i)
            if n is not None:
                num_list.append(str_to_num(i))

        print('В результате преобразований, получили список чисел, которые можно сложить:\n\t', num_list)
        print('Соответственно сумма введённых чисел', str(count) + '-го цикла равна:', sum(num_list))
        summ_0 += sum(num_list)
        print('Тогда общая сумма всех введённых чисел всех циклов равна:', summ_0)
        print('\t', '.' * 30)

        if '#' in str_list:
            print('Так же в', str(count) + '-м цикле Вы ввели специальный символ завершения программы.')
            break


main()

print('*' * 80)

"""Задание .6-7."""

print('\n3.6-7.Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и\n'
      'возвращающую их же, но с прописной первой буквой. Иными словами, в программу должна\n'
      'попадать строка из слов, разделённых пробелом. Каждое слово состоит из латинских букв\n'
      'в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово должно начинаться \n'
      'с заглавной буквы.')
print('-' * 90)


def int_func(text):
    for char in text:
        if (ord(char) >= 97) and ord(char) <= 122:
            print('\t', '.' * 30)
            print('Программа оценила Ваш ввод согласно условию:\n\t', text.title())
            return True
        else:
            print('\t', '.' * 30)
            print('Вы допустили неверный ввод.\n'
                  'Запустите программу вновь, и будте внимательны при вводе.')
            return False


int_func(text=input('Введите строку из слов латинского алфавита разделённых пробелом:\n\t'))

print('*' * 75)
print('END')
