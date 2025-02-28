import time
from getpass import getpass
from login_test import login_test as login
import lib.shared_lib as shared
import utils.datetime_id as id
import os
import traceback

def edit_cert_test(driver, nombre, nuevo_nombre, nivel, precio, recaudo, desc, programas, cambio_gratuito):

    UAC = 1
    passed = 0

    try:

        shared.select_module(driver, 'Ver certificados')
        time.sleep(10)

        shared.search(driver, 'Certificados', nombre)

        shared.click_edit_button(driver, 'Certificados', 0)

        time.sleep(5)

        shared.enter_input_value(driver, 'Nombre', nuevo_nombre)
        shared.select_value(driver, 'Nivel', nivel)
        shared.enter_input_value(driver, 'Precio', precio)
        shared.enter_input_value(driver, 'Recaudo', recaudo)
        shared.enter_textarea_value(driver, 'Descripción', desc)
        shared.multiselect_values(driver, 'Programas', programas)
        shared.press_esc_key(driver)

        if cambio_gratuito:
            shared.click_checkbox(driver, 'Certificado Gratuito')

        time.sleep(5)
        shared.click_button(driver, 'Guardar')
        
        time.sleep(10)
        shared.search(driver, 'Certificados', nombre)

        result = shared.UAC_validate_saved_record(driver, 'Certificados', [nuevo_nombre, nivel, 'Habilitado'], 0)
        passed += shared.evaluate_UAC_result(result)

        print(f'EDIT CERT: {passed}/{UAC} UAC PASSED')

    except Exception as e:
        traceback.print_exc()
        print(f'EDIT CERT: {passed}/{UAC} UAC PASSED')


if __name__ == "__main__":
    driver = shared.init_driver()
    login(driver, input('Username: '), getpass('Password: '))
    shared.select_role(driver, 'Administrador')
    time.sleep(5)
    edit_cert_test(driver, nombre='Mi Certificado 642cde6d', nuevo_nombre='Mi Certificado 642cde6d', nivel='pregrado', precio=10000, recaudo='2023000', desc='UN Certificado', programas=['Ingeniería Agrícola', 'Ingeniería Civil', 'Ingeniería Química'], cambio_gratuito=True)