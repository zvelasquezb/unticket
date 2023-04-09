import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_ingresar_button(driver):
    # Wait for the button with the text "Ingresar a UNTicket" to appear
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Ingresar a UNTicket')]")))

    time.sleep(2) # wait needed for button to be clickable

    # Click the button
    login_button.click()

def UAC_check_unal_domain(driver):
    wait = WebDriverWait(driver, 10)
    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//i[contains(text(), 'unal.edu.co')]")))
        if element is not None:
            return (True, 'unal.edu.co domain is enforced')
        return (False, 'unal.edu.co domain is not enforced')
    except Exception:
        return (False, 'unal.edu.co domain is not enforced')

def login_to_unal_ldap(driver, username, password):
    wait = WebDriverWait(driver, 10)
    # Type the username and password
    username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    username_field.send_keys(username)
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)
    # Click the "Enviar" button
    enviar_button = driver.find_element(By.XPATH, "//button[text()='Enviar']")
    enviar_button.click()

def confirm_google_account(driver):
    wait = WebDriverWait(driver, 10)
    continuar_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Continuar' or text()='Continue']/ancestor::button")))
    continuar_button.click()

def click_use_another_account(driver):
    wait = WebDriverWait(driver, 10)
    # Click the "Use another account" link
    use_another_account = wait.until(EC.presence_of_element_located((By.XPATH, "//li//*[contains(text(), 'Usar otra cuenta') or contains(text(), 'Use another account')]")))
    use_another_account.click()

def UAC_check_google_unal_domain(driver):
    wait = WebDriverWait(driver, 10)
    # Check if there is a span with id "domainSuffix" with text "@unal.edu.co"
    try:
        domain_suffix = wait.until(EC.presence_of_element_located((By.ID, "domainSuffix")))
        if domain_suffix.text == '@unal.edu.co':
            return (True, 'unal.edu.co domain is enforced')
        return (False, 'unal.edu.co domain is not enforced')
    except Exception:
        return (False, 'unal.edu.co domain is not enforced')
    
def login_to_google(driver, username):
    # Type the username
    email_field = driver.find_element(By.XPATH, "//input[@type='email']")
    email_field.send_keys(username)

    # Click the "Next" button
    next_button = driver.find_element(By.XPATH, "//span[text()='Siguiente' or text()='Next']/ancestor::button")
    next_button.click()