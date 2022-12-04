#5.	Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
#Пример:
#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci_list(k: int) -> list:
    fib_list = [-1, 1, 0, 1, 1]
    for i in range(3, k+1):
        fib_list.append(fib_list[-2] + fib_list[-1])
        fib_list.insert(0, fib_list[1] - fib_list[0])
    return fib_list
k = 0
while k < 2:
    k = int(input('Введите число: '))
fib_list = fibonacci_list(k)
print(fib_list)