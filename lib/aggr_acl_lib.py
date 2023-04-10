from selenium.webdriver.common.by import By

def click_solicitud(driver, idx):
  table = driver.find_element(By.XPATH, f"//div[contains(text(), 'Mis Solicitudes')]/following-sibling::div//table")
  tbody = table.find_element(By.TAG_NAME, 'tbody')
  rows = tbody.find_elements(By.TAG_NAME, 'tr')
  if len(rows) > 0:
    row = rows[idx]
    row.click()
  else:
    raise Exception('No records found')

def write_acl(driver, acl):
  # Input field xpath
  input_path= '/html/body/div/div/div/div[1]/div[3]/div/div[1]/div[2]/div/form/div[2]/div/div[7]/div/div/div/div[1]/div[1]/textarea'
  input_field = driver.find_element(By.XPATH, input_path)

  # Type text into the input field
  input_field.send_keys(acl)

  # Input field xpath
  b_path = '/html/body/div/div/div/div[1]/div[3]/div/div[1]/div[2]/div/form/div[3]/button[2]'
  b = driver.find_element(By.XPATH, b_path)
  # Save acl
  b.click()

