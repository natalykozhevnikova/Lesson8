def get_contact():
    name = input('Введите имя: ')
    phone = input('Введите номер: ')
    return f'{name}  {phone}\n'

def find_contact(spravochnik,  req):
    a - ''
    for i in spravochnik:
        if i.find(req) !=-1:
            a = i
    if a == '':
        return "Empty"
    else:
        return a

def get_request():
    return input('Найти контакт:')

def choose_mode():
    return int(input('Выберите режим записи - 1; Выберите режим поиска - 2:'))