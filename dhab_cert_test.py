import time
from getpass import getpass
from login_test import login_test as login
import lib.shared_lib as shared
import utils.datetime_id as id
import os
import traceback

def dhab_cert_test(driver, nombre):

    UAC = 1
    passed = 0

    try:

        shared.select_module(driver, 'Ver certificados')
        time.sleep(10)

        shared.search(driver, 'Certificados', nombre)

        old_status = shared.read_cert_status(driver, 0)
        print(old_status)

        shared.click_eye_button(driver, 'Certificados', 0)

        time.sleep(5)

        shared.search(driver, 'Certificados', nombre)

        new_status = 'Habilitado' if old_status == 'Deshabilitado' else 'Deshabilitado'

        result = shared.UAC_validate_saved_record(driver, 'Certificados', [nombre, None, new_status], 0)
        passed += shared.evaluate_UAC_result(result)

        print(f'DHAB CERT: {passed}/{UAC} UAC PASSED')

    except Exception as e:
        traceback.print_exc()
        print(f'DHAB CERT: {passed}/{UAC} UAC PASSED')


if __name__ == "__main__":
    driver = shared.init_driver()
    login(driver, input('Username: '), getpass('Password: '))
    shared.select_role(driver, 'Administrador')
    time.sleep(5)
    dhab_cert_test(driver, nombre='Mi Certificado 642cdf22')