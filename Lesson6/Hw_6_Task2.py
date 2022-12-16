#Орел и решка
#Дана строка текста, состоящая из букв русского алфавита "О" и "Р".
# Буква "О" – соответствует выпадению Орла, а буква "Р" –
# соответствует выпадению Решки. Напишите программу,
# которая подсчитывает наибольшее количество подряд выпавших Решек.
#Формат входных данных:
#На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
#Формат выходных данных:
#Программа должна вывести наибольшее количество подряд выпавших Решек.
#Примечание. Если выпавших Решек нет, то необходимо вывести число 0.
#Входные данные                                                 Выходные данные
#ОРРОРОРООРРРО                                                       3
#ООООООРРРОРОРРРРРРР                                                 7
#ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР            31


stroka = input().split('О')
res = max(stroka, key=len)
print(len(res))


