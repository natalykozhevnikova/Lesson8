def write_new(contact):
    with open('spravochnik.csv', 'a', encoding='utf8') as f:
        f.write(contact)

def get_spravochnik():
    spravochnik = []
    with open('spravochnik.csv', 'r', encoding='utf8') as f:
        for line in f:
            spravochnik.append(line)
    return spravochnik