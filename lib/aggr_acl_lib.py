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