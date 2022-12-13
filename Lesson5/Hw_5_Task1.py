#1.	Напишите программу, удаляющую из текста все слова, содержащие "абв".
# [‘ПРИВЕТ’, ‘ЗАБВЕНИЕ’, 'ПОКА’] ->[‘ПРИВЕТ’, 'ПОКА’]


a = input()
def del_some_words(a):
    a = list(filter(lambda x:'абв' not in x, a.split))
    return ' '.join(a)
a = del_some_words(a)

print(a)