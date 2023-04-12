import time
import lib.aggr_acl_lib as aggr_acl
from login_test import login_test as login
from getpass import getpass
import lib.shared_lib as shared
import utils.filters as filters
import traceback

# Test de agregar aclaracion - solicitante
def nuevo_ticket_test(driver, programa, certificado, Observaciones,num_consig):

  UAC = 1
  passed = 0

  try:
    original_window = driver.current_window_handle
    # Add clarification
    shared.select_module(driver, 'Nuevo ticket')
    time.sleep(5)
    

    #time.sleep(5)
    shared.select_value(driver, 'Programa', programa)
    shared.select_value(driver, 'Certificado', certificado)
    shared.enter_input_value(driver, 'Observaciones', Observaciones)
    shared.click_checkbox(driver, '¡Quiero que mi certificado sea digital!')
    time.sleep(2)
    shared.click_button(driver, 'Continuar')
    time.sleep(3)
    shared.click_button(driver, 'Continuar')
    time.sleep(2)
    shared.enter_input_value(driver, 'Número de consignación', num_consig)  # spelling error
    shared.enter_input_value(driver, 'Soporte de pago', os.path.abspath(r'utils\files\soporte.pdf'))
    shared.select_value(driver, 'Tipo de pago', programa)
    shared.click_button(driver, 'Pagar')
    print(f'AGGR ACL: {passed}/{UAC} UAC PASSED')
  except Exception as e:
    traceback.print_exc()
    print(f'AGGR ACL: {passed}/{UAC} UAC PASSED')

if __name__ == '__main__':
  certificados=["Plan de estudio extenso pregrado","Certificado egresado pregrado",
                "Certificado con otra información egresado pregrado",
                "Certificado con otra información estudiante pregrado",
                "Certificado de notas retirado o en reserva de cupo pregrado",
                "Duplicado de diploma y acta de grado pregrado",
                "Plan de estudio resumido pregrado",
                "Certificado de estudio retirado o en reserva de cupo pregrado",
                "Certificado de notas egresado pregrado"]
  Tipo_de_pago=["Banco",
                "Pago Virtual"]
  driver = shared.init_driver()
  login(driver, input('Username: '), getpass('Password: '))
  shared.select_role(driver, 'Solicitante')
  nuevo_ticket_test(driver, programa='Ingeniería de Sistemas y Computación', certificado=certificados[0],Observaciones="hola")


