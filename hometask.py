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

from functools import reduce

list1 = [-1, 3, 7, 99, 0]

print(reduce(lambda x, y: x if x > y else y, list1))   #   max
print(reduce(lambda x, y: x if x < y else y, list1))   #   min

'''Написать функцию, которая определяет, является ли год високосным. Пользователь вводит год, если он високосный,
 то функция возвращает True. Если нет, то False.'''


def big_year(y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        return True
    else:
        return False


print(big_year(2000))









