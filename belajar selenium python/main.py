import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):
  def setUp(self):
    self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
  def test_a_success_login(self):
    driver = self.browser #buka web browser
    driver.get("https://www.saucedemo.com/") # buka situs
    time.sleep(2)
    driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
    time.sleep(0.5)
    driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
    time.sleep(0.5)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)
    
    response_data = driver.find_element(By.CLASS_NAME,"title").text # validasi
    self.assertIn('PRODUCTS', response_data)
    
  def test_a_failed_login(self):
    driver = self.browser #buka web browser
    driver.get("https://www.saucedemo.com/") # buka situs
    time.sleep(2)
    driver.find_element(By.ID,"user-name").send_keys("strange_user") # isi email
    time.sleep(0.5)
    driver.find_element(By.ID,"password").send_keys("random_sauce") # isi password
    time.sleep(0.5)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)
    
    response_data = driver.find_element(By.CSS_SELECTOR,"h3[data-test='error']").text # validasi
    self.assertIn('Epic sadface: Username and password do not match any user in this service', response_data)

  def tearDown(self):
    self.browser.close()



class TestRegister(unittest.TestCase):
  #jika gagal, berarti sudah pernah register  
  def setUp(self):
    self.browser = webdriver.Chrome(ChromeDriverManager().install())
  
  def test_register(self):
    driver = self.browser
    driver.get("http://barru.pythonanywhere.com/daftar")
    time.sleep(2)
    driver.find_element(By.ID,"signUp").click()
    time.sleep(1.5)
    #register
    driver.find_element(By.ID,"name_register").send_keys("Agus2")
    time.sleep(0.5)
    driver.find_element(By.ID,"email_register").send_keys("Agus2@tree.in")
    time.sleep(0.5)
    driver.find_element(By.ID,"password_register").send_keys("password")
    time.sleep(0.5)
    driver.find_element(By.ID,"signup_register").click()
    time.sleep(1)
    
    isSuccessRegister = driver.find_element(By.ID,"swal2-title").text
    self.assertIn('berhasil', isSuccessRegister)
    
  def tearDown(self):
    self.browser.close()




if __name__ == "__main__":
  unittest.main()
