import time
from getpass import getpass
from login_test import login_test as login
import lib.shared_lib as shared
import utils.datetime_id as id
import traceback

def aggr_cert_test(driver, nombre, precio, recaudo, desc, nivel, programas, gratuito):

    UAC = 2
    passed = 0

    try:

        shared.select_module(driver, 'Ver certificados')
        time.sleep(2)
        shared.click_button(driver, 'Agregar')
        time.sleep(2)
        shared.enter_input_value(driver, 'Nombre', nombre)
        shared.select_value(driver, 'Nivel', nivel)
        shared.enter_input_value(driver, 'Precio', precio)
        shared.enter_input_value(driver, 'Recaudo', recaudo)
        shared.enter_textarea_value(driver, 'Descripción', desc)
        shared.multiselect_values(driver, 'Programas', programas)
        shared.press_esc_key(driver)
        if gratuito:
            shared.click_checkbox(driver, 'Certificado Gratuito')
        shared.click_button(driver, 'Guardar')
        time.sleep(5)
        shared.search(driver, 'Certificados', nombre)
        result = shared.UAC_check_unique_record(driver, 'Certificados', nombre)
        passed += shared.evaluate_UAC_result(result)
        result = shared.UAC_validate_saved_record(driver, 'Certificados', [nombre, nivel, 'Habilitado'], 0)
        passed += shared.evaluate_UAC_result(result)

        print(f'AGGR CERT: {passed}/{UAC} UAC PASSED')

    except Exception as e:
        traceback.print_exc()
        print(f'AGGR CERT: {passed}/{UAC} UAC PASSED')

if __name__ == "__main__":
    driver = shared.init_driver()
    login(driver, input('Username: '), getpass('Password: '))
    shared.select_role(driver, 'Administrador')
    time.sleep(5)
    aggr_cert_test(driver, nombre=f'Mi Certificado {id.get_id()}', precio=10000, recaudo='2023000', desc='UN Certificado', nivel='pregrado', programas=['Ingeniería Agrícola', 'Ingeniería Civil'], gratuito=True)
    