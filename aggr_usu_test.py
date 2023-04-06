import time
from getpass import getpass
from login_test import login_test as login
import lib.shared_lib as shared
import utils.datetime_id as id

def aggr_usu_test(driver, username, nombres, apellidos, tipo_doc, num_doc, roles):

    UAC = 2
    fails = 0

    try:

        shared.select_module(driver, 'Administrar usuarios')
        time.sleep(2)
        shared.click_button(driver, 'Agregar')
        time.sleep(2)
        shared.enter_input_value(driver, 'Username', username)
        shared.enter_input_value(driver, 'Nombres', nombres)
        shared.enter_input_value(driver, 'Apellidos', apellidos)
        shared.select_value(driver, 'Tipo de documento', tipo_doc)
        shared.enter_input_value(driver, 'Documento', num_doc)
        shared.multiselect_values(driver, 'Roles', roles)
        shared.press_esc_key(driver)
        shared.click_button(driver, 'Guardar')
        time.sleep(5)
        shared.search(driver, 'Usuarios', username)
        result = shared.UAC_check_unique_record(driver, 'Usuarios', username)
        fails += shared.evaluate_UAC_result(result)
        result = shared.UAC_validate_saved_record(driver, 'Usuarios', [username, ' '.join(roles)])
        fails += shared.evaluate_UAC_result(result)

        print(f'AGGR USU: {UAC - fails}/{UAC} UAC PASSED')

    except Exception as e:
        print(str(e))
        print(f'AGGR USU: {UAC - fails}/{UAC} UAC PASSED')

if __name__ == "__main__":
    driver = shared.init_driver()
    login(driver, input('Username: '), getpass('Password: '))
    shared.select_role(driver, 'Administrador')
    time.sleep(5)
    aggr_usu_test(driver, username=f'alicia{id.get_id()}', nombres='Alicia', apellidos='Smith', tipo_doc='C.C.', num_doc=f'{id.get_id_()}', roles=['Solicitante', 'Recepción'])
    