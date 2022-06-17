# # №1
# print('Hello, World!')
# #просто ввод
# a = int(input())
# print(a**2)

# # метод format() = помещает значение каждого аргумента в обозначенное место
# age = 26
# name = 'Swaroop'
# print('Возвраст {0} - -  {1} лет'.format(name, age))
# print('Почему {0} забавляется с этим Python?'.format(name))

# # Код возвращает истину, если аргумент — нечётное число и ложь, если чётное.
# # Т.к. 20 — чётное, то и возвращаетесь False. Соответственно, т.к. 21 — нечётное, получается True.
# f = lambda x: bool(x % 2) #bool() приводит переданный аргумент к типу булева, соответственно, 20 % 2 будет 0 а 21%2 даст остаток 1. Ноль приведённый к булева даёт False, а любое число, приведённое к булева True.
# print(f(20), f(21))

#print(9//2)# возвращает целую часть числа с плавающей запятой

# a = [10, 20]
# b = a
# b += [30, 40]
# print(a)
# print(b) #Т.к. b и а отсылаются к одному объекту, использование += на b меняет значение и a, и b.

# x = "Питон: задачки и вопросы"[0]
# print(x) # возвращает первый символ строки

# lst = [-2, -1, 0, 1, 2]
# def fnc(x):
#     return x < 1
# rst = filter(fnc, lst)
# print(list(rst))

# import time # ищем, какая функция сработает быстрее
#
# n = 100000000
#
# def fast_function(n):
#     a = list(i for i in range(n))
#     n in a
#
# def very_fast_function(n):
#     b = (i for i in range(n))
#     n in b
#
# def super_very_fast_function(n):
#     c = set(i for i in range(n))
#     n in c
#
# def the_super_very_fast_function(n):
#     d = {i for i in range(n)}
#     n in d
#
# def monitoring(func):
#     tic = time.perf_counter()
#     func(n)
#     toc = time.perf_counter()
#     print(f"{func.__name__} {toc - tic:0.4f} seconds")
# monitoring(fast_function)
# monitoring(very_fast_function)
# monitoring(super_very_fast_function)
# monitoring(the_super_very_fast_function)

# class pyq:
#     def __init__(self,id):
#         self.id = id
#         id = 42
# var_ = pyq(21)
# print(var_.id)

# print(0.1 + 0.2 == 0.4)# ответ = 0.30000000000000004, поэтому false


