import logger
import model

while True:
    mode = model.choose_mode()
    if mode == 1:
        logger.write_new(model.get_contact())
    elif mode == 2:
        contact = model.get_request()
        spravochnik = logger.get_spravochnik()
        print(model.find_contact(spravochnik, contact))
    elif mode == 0:
        print('Выход')
        break
