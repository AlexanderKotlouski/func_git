''' Создадим пустую функцию которая ничего не возвращает.'''

def empty_function():
    pass

''' Написать функцию, которая принимает число, возвращает его значение умноженное на два.'''

def add(a):
    return a*2

print(add(10))

''' Напишем функцию,которая определяет параметр на чётность. Если чётное число принтим (‘yes’) в ином случае (‘no’).'''

def even_number(a):
    if a%2==0:
        return 'yes'
    else:
        return 'no'
print(even_number(19))

'''Пишем функцию, принимающую два аргумента. После чего проверим, если первое число больше 10, принтим (‘да’).
 Если меньше(‘нет’).'''


def compare_number(a, b):
    if a > 10:
        return 'yes'
    else:
        return 'no'
print(compare_number(9,20))


'''Написать лямбда функцию, которая делит по модулю( % ) два аргумента.'''

f = lambda x, y: x % y

print(f(10, 6))

'''Создадим функцию с простыми командами. Обернём её в декоратор, который бы дополнял возможности функции.'''


def decorator(say_greeting):
    def compare_number(a, b):
        say_greeting()
        if a > 10:
            return 'yes'
        else:
            return 'no'

    print(compare_number(9, 20))


@decorator
def say_greeting():
    print('Hello')


'''Использовать функцию map и filter'''


print(list(map(lambda x : x*2, [1, 2, 3, 4])))


a = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x : x % 2 == 0, a)))

'''Сделать функцию поиска минимума и максимума в списке.'''







