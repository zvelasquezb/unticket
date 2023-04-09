# basarse en edit_dat_test y en des_arch_test para validar nombre de archivo
import time
from selenium.webdriver.common.by import By
from getpass import getpass
from login_test import login_test as login
import lib.shared_lib as shared
import lib.edit_dat_lib as edit_dat
import utils.datetime_id as id
import os
import traceback

def gen_rep_test(driver, program_action, periodo_academico,f_inicio,f_final):

    UAC = 1
    passed = 0

    try:

        shared.select_module(driver, 'Generar reporte')
        time.sleep(5)

        if program_action == 1:
            shared.select_value(driver, 'Periodo Académico', periodo_academico)
            time.sleep(5)
            shared.click_button(driver, 'Generar')
            time.sleep(5)
        elif program_action == 2:
            shared.click_button(driver, 'reporte histórico')
            time.sleep(5)
        elif program_action == 3:
            shared.click_button(driver, 'reporte periodo actual')
            time.sleep(5)
        elif program_action == 4:
            shared.set_date_field_value(driver,1,'Inicio', f_inicio,idx=0)
            time.sleep(5)
            shared.set_date_field_value(driver,1,'Final', f_final,idx=0)
            time.sleep(5)
            shared.click_button_2(driver, 'Generar')

            time.sleep(5)



    except Exception as e:
        traceback.print_exc()
        print(f'EDIT DAT: {passed}/{UAC} UAC PASSED')


if __name__ == "__main__":
    driver = shared.init_driver()
    login(driver, input('Username: '), getpass('Password: '))
    time.sleep(10)
    shared.select_role(driver, 'Administrador')
    time.sleep(5)
    # 0 : nothing
    # 1 : Reporte periodo academico
    # 2 : Reporte Historico
    # 3 : Reporte Periodo Actual
    # 4 : Reporte por fechas
    
    gen_rep_test(driver, program_action=1, periodo_academico='2023-1', f_inicio='2023/04/04',f_final='2023/04/08')
    #gen_rep_test(driver, program_action=2, periodo_academico='2023-1', f_inicio='2023/04/04',f_final='2023/04/08')
    #gen_rep_test(driver, program_action=3, periodo_academico='2023-1', f_inicio='2023/04/04',f_final='2023/04/08')
    #gen_rep_test(driver, program_action=4, periodo_academico='2023-1', f_inicio='2023/04/04',f_final='2023/04/08')