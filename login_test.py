import time

from getpass import getpass
import lib.login_lib as login
import lib.shared_lib as shared

def login_test(driver, username, password):

    UAC = 4
    passed = 0

    try:

        shared.go_to_url(driver, 'bienvenida')
        
        login.click_ingresar_button(driver)
        
        time.sleep(1)

        shared.switch_to_window(driver, 1)
        
        time.sleep(2)
        
        # User Acceptance Criteria Check
        result = login.UAC_check_unal_domain(driver)
        passed += shared.evaluate_UAC_result(result)
        
        login.login_to_unal_ldap(driver, username, password)
        
        time.sleep(5)
        
        login.confirm_google_account(driver)
        
        time.sleep(3)

        login.click_use_another_account(driver)

        time.sleep(3)
        
        # User Acceptance Criteria Check
        result = login.UAC_check_google_unal_domain(driver)
        passed += shared.evaluate_UAC_result(result)

        login.login_to_google(driver, username)

        time.sleep(2)

        # User Acceptance Criteria Check
        result = login.UAC_check_unal_domain(driver)
        passed += shared.evaluate_UAC_result(result)
        
        
        login.login_to_unal_ldap(driver, username, password)

        time.sleep(10)

        shared.switch_to_window(driver, 0)

        # User Acceptance Criteria Check
        result = shared.UAC_check_current_url(driver, 'perfil')
        passed += shared.evaluate_UAC_result(result)

        print(f'LOGIN: {passed}/{UAC} UAC PASSED')

    except Exception as e:
        print(str(e))
        print(f'LOGIN: {passed}/{UAC} UAC PASSED')

if __name__ == "__main__":
    driver = shared.init_driver()
    login_test(driver, input('Username: '), getpass('Password: '))
