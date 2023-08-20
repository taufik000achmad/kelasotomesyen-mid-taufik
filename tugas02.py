from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(30)
url_demoqa = 'https://demoqa.com/webtables'

driver.get(url_demoqa)
wait = WebDriverWait(driver, 10)

driver.find_element(By.ID,'addNewRecordButton').click()


driver.find_element(By.ID,'firstName').send_keys('Bambang')
driver.find_element(By.ID,'lastName').send_keys('Pamungkas')
driver.find_element(By.ID,'userEmail').send_keys('Pamungkas@gmail.com')
driver.find_element(By.ID,'age').send_keys('Pamungkas@gmail.com')
driver.find_element(By.ID,'salary').send_keys('20')
driver.find_element(By.ID,'department').send_keys('kesejahteraan indonesia')
driver.find_element(By.XPATH,"//button[@id='submit']").click()



driver.quit()
