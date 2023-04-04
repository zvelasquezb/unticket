from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from utils.urls import URLs

def init_driver():
    # Create a new instance of the Chrome driv
    options = webdriver.ChromeOptions()
    options.add_argument('--log-level=3') # set log level to SEVERE
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver

def go_to_url(driver, urlkey):
    url = URLs[urlkey]
    # Go to the URL
    driver.get(url)

def switch_to_window(driver, idx):
    # Switch to the new window
    driver.switch_to.window(driver.window_handles[idx])

def quit_driver(driver):
    # Close the browser window
    driver.quit()

def UAC_check_current_url(driver, urlkey):
    url = URLs[urlkey]
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(EC.url_to_be(url))
        if driver.current_url == url:
            return (True, f'{urlkey} reached')
        else:
            return (False, f'{urlkey} not reached')
    except Exception:
        return (False, f'{urlkey} not reached')
    
def UAC_check_redirection(driver, urlkey1, urlkey2):
    url1 = URLs[urlkey1]
    url2 = URLs[urlkey2]
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(EC.url_to_be(url2))
        if driver.current_url == url2:
            return (True, f'successful redirection from {urlkey1} to {urlkey2}')
        else:
            return (False, f'failed redirection from {urlkey1} to {urlkey2}')
    except Exception:
        return (False, f'failed redirection from {urlkey1} to {urlkey2}')
    
def select_role(driver, role):
    element = driver.find_element_by_css_selector('div.v-select__selections > input[type="text"]')

    # Create a Select object from the element
    select = Select(element)

    # Select an option by value
    select.select_by_value(role)

def evaluate_UAC_result(result):
    if result[0] == True:
        print('UAC PASSED:', result[1])
        return 0
    else:
        print('UAC FAILED:', result[1])
        return 1