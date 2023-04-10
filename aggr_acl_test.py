import time
from lib.aggr_acl_lib import click_solicitud, write_acl
from login_test import login_test as login
from getpass import getpass
import lib.shared_lib as shared

# Test de agregar aclaracion como solicitante
def aggr_acl(driver, keyword, acl):
  shared.select_role(driver, 'Solicitante')
  UAC = 0
  passed = 0

  try:
    shared.select_module(driver, 'Mis solicitudes')
    time.sleep(5)
    
    shared.search(driver, 'Solicitudes', keyword)
    time.sleep(5)

    click_solicitud(driver, 0)
    time.sleep(5)

    write_acl(driver, acl)
    time.sleep(5)

    print(f'aggr_acl_test COMPLETED: {passed}/{UAC} UAC PASSED')
  except Exception as e:
    traceback.print_exc()
    print(f'aggr_acl_test FAILED: {passed}/{UAC} UAC PASSED')

if __name__ == '__main__':
  driver = shared.init_driver()
  login(driver, input('Username: '), getpass('Password: '))
  aggr_acl(driver, keyword='1512', acl='prueba 1234')



