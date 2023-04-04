from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_cerrar_sesion_button(driver):
    # Wait for the button with the text "Ingresar a UNTicket" to appear
    wait = WebDriverWait(driver, 10)
    logout_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Cerrar sesión')]")))
    logout_button.click()