from selenium.webdriver.common.by import By
import time

def open_edit_program_modal(driver, program):
    try:
        row = driver.find_element(By.XPATH, f"//td[contains(text(), '{program}')]/ancestor::tr")
        button = row.find_elements(By.TAG_NAME, 'button')[0]      
        button.click()
    except:
        raise Exception('Program not found')
    
def open_delete_program_modal(driver, program):
    try:
        row = driver.find_element(By.XPATH, f"//td[contains(text(), '{program}')]/ancestor::tr")
        button = row.find_elements(By.TAG_NAME, 'button')[1]      
        button.click()
    except:
        raise Exception('Program not found')

def see_all_programs(driver):
    select_elem = driver.find_element(By.XPATH, "//div[@class='v-data-footer__select']//div[@class='v-select__slot']")
    select_elem.click()
    time.sleep(2)
    # Locate the desired value and click on it
    value = driver.find_element(By.XPATH, f"//div[contains(@class, 'menuable__content__active')]//div[contains(text(),'All')]")
    value.click()