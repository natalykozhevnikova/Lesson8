# 3.	Реализуйте алгоритм задания случайных чисел
# без использования встроенного генератора псевдослучайных чисел.
#Подсказка: можно использовать модуль datetime

import time

def myrandom(n):
    str_time = str(time.time())
    str_time = str_time.replace('.', '')
    number = int(str_time) % n
    return number
print(myrandom(100))



