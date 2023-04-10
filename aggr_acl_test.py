import time
from lib.aggr_acl_lib import click_solicitud, write_acl
from login_test import login_test as login
from getpass import getpass
import lib.shared_lib as shared
import utils.filters as filters

# Test de agregar aclaracion - solicitante
def aggr_acl(driver, filter, keyword, acl, expected):

  UAC = 1
  passed = 0

  try:
    # Add clarification
    shared.select_module(driver, 'Mis solicitudes')
    time.sleep(5)
    
    shared.search(driver, 'Solicitudes', keyword)
    time.sleep(5)
    
    click_solicitud(driver, 0)
    time.sleep(5)

    write_acl(driver, acl)
    time.sleep(5)
  
    # Check if request's state has changed 
    shared.search(driver, 'Solicitudes', keyword)
    result = shared.UAC_check_search_results(driver, 'Solicitudes', keyword, filter['column'], filter['unique'], expected)
    passed += shared.evaluate_UAC_result(result)

    print(f'aggr_acl_test COMPLETED: {passed}/{UAC} UAC PASSED')
  except Exception as e:
    traceback.print_exc()
    print(f'aggr_acl_test FAILED: {passed}/{UAC} UAC PASSED')

if __name__ == '__main__':
  driver = shared.init_driver()
  login(driver, input('Username: '), getpass('Password: '))
  shared.select_role(driver, 'Solicitante')
  aggr_acl(driver, filter=filters.FILTERS['solicitudes']['id'], keyword='1512', acl='prueba 1234', expected='En trámite')



