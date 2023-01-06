import pupil_info as pu
import class_info as cl


def option():
    print("\nДобрый день!")
    ch = int(input('Введите действие: \n \
    1: Поиск ID ученика по имени \n \
    2: Узнать класс  и место в классе, за которым сидит ученик \n \
    3: Выход\n \
    Ваш выбор: '))

    if ch == 1:
        Surn = str(input("Введите имя ученика: "))
        if Surn in pu.stud_card['Имя']:
            index = pu.stud_card['Имя'].index(Surn)
        print(f"{pu.stud_card['ID'][index]}, {pu.stud_card['Имя'][index]},{pu.stud_card['Фамилия'][index]}\n,{pu.stud_card['Дата рождения'][index]}, {pu.stud_card['Успеваемость'][index]}")
        print('\nХотите выбрать другое действие? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            option()
        exit()

    elif ch == 2:
        c = input('Введите ID ученика для вывода по классам: ')
        if c in cl.class_card['ID']:
            index = cl.class_card['ID'].index(c)
            print(f" Сидит в классе - {cl.class_card['Предмет'][index]}\n\, за партой номер - {cl.class_card['Номер парты'][index]}, это {cl.class_card['Ряд'][index]}, парта - {cl.class_card['Вид парты'][index]}, Имя: {pu.stud_card['Имя'][index]}, Фамилия - {pu.stud_card['Фамилия'][index]}, и успеваемасть у ученика: {pu.stud_card['Успеваемость'][index]}")
            print('\nХотите выполнить другую операцию??? Y или N: ')
            num = input()
            if num == 'Y' or 'y' or 'У' or 'у':
                option()
            exit()
    else:
        print('еще раз')
    exit()


option()