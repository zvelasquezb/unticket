import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass


def test_login(username, password):
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Go to the URL
    driver.get("https://procesofibog.unal.edu.co/unticket/")

    # Wait for the button with the text "Ingresar a UNTicket" to appear
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Ingresar a UNTicket')]")))

    time.sleep(2) # wait needed for button to be clickable

    # Click the button
    login_button.click()

    # Switch to the new window
    original_window = driver.current_window_handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)

    time.sleep(2)

    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//i[contains(text(), 'unal.edu.co')]")))
        assert element is not None, "Element not found"
        print("Element found")
    except Exception:
        print("Element not found")
        assert False, "Element not found"

    # Type the username and password
    username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    username_field.send_keys(username)
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)

    # Click the "Enviar" button
    enviar_button = driver.find_element(By.XPATH, "//button[text()='Enviar']")
    enviar_button.click()

    time.sleep(5)
    continuar_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Continuar']/ancestor::button")))
    print(continuar_button.text)
    continuar_button.click()

    time.sleep(3)

    # Click the "Use another account" link
    use_another_account = wait.until(EC.presence_of_element_located((By.XPATH, "//li//*[contains(text(), 'Usar otra cuenta')]")))
    use_another_account.click()

    time.sleep(3)
    
    # Check if there is a span with id "domainSuffix" with text "@unal.edu.co"
    domain_suffix = wait.until(EC.presence_of_element_located((By.ID, "domainSuffix")))
    assert domain_suffix.text == "@unal.edu.co", "Domain suffix is not @unal.edu.co"

    # Type the username
    email_field = driver.find_element(By.XPATH, "//input[@type='email']")
    email_field.send_keys(username)

    # Click the "Next" button
    next_button = driver.find_element(By.XPATH, "//span[text()='Siguiente']/ancestor::button")
    next_button.click()

    time.sleep(2)

    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, "//i[contains(text(), 'unal.edu.co')]")))
        assert element is not None, "Element not found"
        print("Element found")
    except Exception:
        print("Element not found")
        assert False, "Element not found"

    # Type the username and password
    username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
    username_field.send_keys(username)
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)

    # Click the "Enviar" button
    enviar_button = driver.find_element(By.XPATH, "//button[text()='Enviar']")
    enviar_button.click()

    time.sleep(10)

    # Switch to the new window
    driver.switch_to.window(original_window)

    # Wait for the profile page to load
    profile_url = "https://procesofibog.unal.edu.co/unticket/perfil"
    wait.until(EC.url_to_be(profile_url))

    # Assert if the current URL is the profile URL
    assert driver.current_url == profile_url, "Login failed"

    # Close the browser window
    driver.quit()

    print('Success')

test_login(input('Username: '), getpass('Password: '))
