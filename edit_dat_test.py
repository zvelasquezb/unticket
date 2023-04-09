import time
from getpass import getpass
from login_test import login_test as login
import lib.shared_lib as shared
import lib.edit_dat_lib as edit_dat
import utils.datetime_id as id
import os
import traceback

def edit_dat_test(driver, program_action, tipo_doc, num_doc, program_data=None):

    UAC = 0
    passed = 0

    try:

        shared.select_module(driver, 'Mis datos')

        shared.click_button(driver, 'Modificar')

        shared.select_value(driver, 'Tipo de documento', tipo_doc)
        shared.enter_input_value(driver, 'Número', num_doc)

        if program_action == 1:
            shared.click_button(driver, 'Agregar')
            shared.select_value(driver, 'Estado solicitante', program_data[1])
            shared.select_value(driver, 'Programa', program_data[0])

            if program_data[1] != 'Estudiante Activo':
                shared.set_date_field_value(driver, 0, 'Año de grado / Año de retiro', program_data[2])

            shared.click_button(driver, 'Guardar', 1)

        elif program_action == 2:
            edit_dat.see_all_programs(driver)
            edit_dat.open_edit_program_modal(driver, program_data[0])
            time.sleep(10)

        elif program_action == 3:
            edit_dat.see_all_programs(driver)
            edit_dat.open_delete_program_modal(driver, program_data[0])
            shared.click_button(driver, 'Eliminar')
            time.sleep(10)


        shared.click_button(driver, 'Guardar')

        time.sleep(10)

        print(f'EDIT DAT: {passed}/{UAC} UAC PASSED')

    except Exception as e:
        traceback.print_exc()
        print(f'EDIT DAT: {passed}/{UAC} UAC PASSED')


if __name__ == "__main__":
    driver = shared.init_driver()
    login(driver, input('Username: '), getpass('Password: '))
    shared.select_role(driver, 'Administrador')
    time.sleep(5)
    # 0 : nothing
    # 1 : add
    # 2 : edit
    # 3 : delete
    edit_dat_test(driver, program_action=1, tipo_doc='C.C.', num_doc='1070000000', program_data=['Ingeniería Agrícola', 'Egresado', '2023-01-03'])
    #edit_dat_test(driver, program_action=3, tipo_doc='C.C.', num_doc='1070000000', program_data=['Ingeniería Eléctrica', 'Estudiante Activo', None])
    #edit_dat_test(driver, program_action=1, tipo_doc='C.C.', num_doc='1070000000', program_data=['Ingeniería Mecánica', 'Estudiante Activo', None])
    #edit_dat_test(driver, program_action=2, tipo_doc='C.C.', num_doc='1070000000', program_data=['Ingeniería Agrícola', 'Estudiante Activo', None])
    #edit_dat_test(driver, program_action=0, tipo_doc='C.C.', num_doc='1070000000')