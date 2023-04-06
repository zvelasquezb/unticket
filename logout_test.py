import time
from getpass import getpass
from login_test import login_test as login
from utils.urls import URLs
import lib.logout_lib as logout
import lib.shared_lib as shared

def logout_test(driver):

    UAC = 11
    fails = 0

    try:

        logout.click_cerrar_sesion_button(driver)

        time.sleep(2)

        # User Acceptance Criteria Check
        result = shared.UAC_check_current_url(driver, 'bienvenida')
        fails += shared.evaluate_UAC_result(result)

        for urlkey in URLs.keys():

            if urlkey == 'bienvenida':
                continue

            shared.go_to_url(driver, urlkey)
            time.sleep(1)

            # User Acceptance Criteria Check
            result = shared.UAC_check_redirection(driver, urlkey, 'bienvenida')
            fails += shared.evaluate_UAC_result(result)

        print(f'LOGOUT: {UAC - fails}/{UAC} UAC PASSED')

    except Exception as e:
        print(str(e))
        print(f'LOGOUT: {UAC - fails}/{UAC} UAC PASSED')

if __name__ == "__main__":
    driver = shared.init_driver()
    login(driver, input('Username: '), getpass('Password: '))
    logout_test(driver)