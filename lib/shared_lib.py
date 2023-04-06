import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.urls import URLs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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
    # Click on the dropdown list
    dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='v-select__selections']")))
    dropdown.click()
    # Locate the desired value and click on it
    value = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(),'{role}')]")))
    value.click()

def evaluate_UAC_result(result):
    if result[0] == True:
        print('UAC PASSED:', result[1])
        return 0
    else:
        print('UAC FAILED:', result[1])
        return 1
    
def select_module(driver, module):
    # find the element by the link text "Ver certificados"
    element = driver.find_element(By.XPATH, f"//div[text()='{module}']/ancestor::a")

    # click the element
    element.click()

def click_button(driver, text):
    # find the element by the link text "Ver certificados"
    element = driver.find_element(By.XPATH, f"//span[contains(text(),'{text}')]/ancestor::button")

    # click the element
    element.click()

def enter_input_value(driver, label, value):
    # Find the label element with the matching text
    label_element = driver.find_element(By.XPATH, f"//label[contains(text(),'{label}')]")

    # Find the input element next to the label
    input_element = label_element.find_element(By.XPATH, "./following-sibling::input")

    # Enter the desired value into the input element
    input_element.send_keys(value)

def enter_textarea_value(driver, label, value):
    # Find the label element with the matching text
    label_element = driver.find_element(By.XPATH, f"//label[contains(text(),'{label}')]")

    # Find the input element next to the label
    input_element = label_element.find_element(By.XPATH, "./following-sibling::textarea")

    # Enter the desired value into the input element
    input_element.send_keys(value)

def select_value(driver, label, value):
    dropdown = driver.find_element(By.XPATH, f"//label[contains(text(),'{label}')]/following-sibling::div[@class='v-select__selections']")
    dropdown.click()
    # Locate the desired value and click on it
    value = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(),'{value}')]")))
    value.click()

def multiselect_values(driver, label, values):
    dropdown = driver.find_element(By.XPATH, f"//label[contains(text(),'{label}')]/following-sibling::div[@class='v-select__selections']")
    dropdown.click()
    # Locate the desired value and click on it
    for value in values:
        checkbox = driver.find_element(By.XPATH, f"//div[contains(text(),'{value}')]/ancestor::div/preceding-sibling::div[contains(@class, 'v-list-item__action')]/div[contains(@class, 'v-simple-checkbox')]")
        checkbox.click()

def click_checkbox(driver, label):
    checkbox = driver.find_element(By.XPATH, f"//label[contains(text(), '{label}')]/preceding-sibling::div//input[@type='checkbox']/following-sibling::div")
    checkbox.click()

def press_esc_key(driver):
    # Create an ActionChains instance
    actions = ActionChains(driver)
    # Simulate pressing the ESC key
    actions.send_keys(Keys.ESCAPE).perform()

def search(driver, label, value):
    # Find the input field within the div element of text "text"
    input_field = driver.find_element(By.XPATH, f"//div[contains(text(), '{label}')]//input")

    # Type text into the input field
    input_field.send_keys(value)

def UAC_check_unique_record(driver, tablename, value):
    table = driver.find_element(By.XPATH, f"//div[contains(text(), '{tablename}')]/following-sibling::div//table")
    tbody = table.find_element(By.TAG_NAME, 'tbody')
    rows = tbody.find_elements(By.TAG_NAME, 'tr')
    if len(rows) == 1:
        return (True, f'1 record found for {value}')
    return (False, f'multiple records found for {value}')


def UAC_validate_saved_record(driver, tablename, values):
    table = driver.find_element(By.XPATH, f"//div[contains(text(), '{tablename}')]/following-sibling::div//table")
    tbody = table.find_element(By.TAG_NAME, 'tbody')
    rows = tbody.find_elements(By.TAG_NAME, 'tr')
    if len(rows) > 0:
        row = rows[0]
        tds = row.find_elements(By.TAG_NAME, 'td')
        tds = tds[:len(values)]
        if len(tds) > 0:
            for td, value in zip(tds, values):
                if ' '.join(sorted(td.text.lower().split())) != ' '.join(sorted(value.lower().split())):
                    return (False, f"mismatch between {' '.join(td.text.lower().split().sort())} and {' '.join(value.lower().split().sort())}")
            return (True, f"record data match with [{', '.join(values)}]")
    return (False, f"no records found for [{', '.join(values)}]")