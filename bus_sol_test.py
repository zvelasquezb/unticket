import time
from getpass import getpass
from login_test import login_test as login
import lib.shared_lib as shared
import utils.datetime_id as id
import os
import traceback
import utils.filters as filters

def bus_sol_test(driver, filter, keyword, expected):
    
    UAC = 1
    passed = 0

    try:

        shared.select_module(driver, 'Solicitudes')
        time.sleep(10)

        shared.search(driver, 'Solicitudes', keyword)

        time.sleep(5)

        result = shared.UAC_check_search_results(driver, 'Solicitudes', keyword, filter['column'], filter['unique'], expected)
        passed += shared.evaluate_UAC_result(result)

        print(f'EDIT SOL: {passed}/{UAC} UAC PASSED')

    except Exception as e:
        traceback.print_exc()
        print(f'EDIT SOL: {passed}/{UAC} UAC PASSED')

if __name__ == "__main__":
    driver = shared.init_driver()
    login(driver, input('Username: '), getpass('Password: '))
    shared.select_role(driver, 'Administrador')
    time.sleep(5)
    bus_sol_test(driver, filter=filters.FILTERS['solicitudes']['id'], keyword='1511', expected=True)
    bus_sol_test(driver, filter=filters.FILTERS['solicitudes']['id'], keyword='3000', expected=False)
    bus_sol_test(driver, filter=filters.FILTERS['solicitudes']['username'], keyword='Zamir', expected=True)