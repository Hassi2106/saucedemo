from selenium.webdriver.common.by import By


class swag:
       def __init__(self, driver):
           self.driver = driver
           self.username_id = 'user-name'
           self.password_id = 'password'
           self.lon_id = 'login-button'
           self.cart_id = 'add-to-cart-sauce-labs-backpack'
           self.filter_XPATH = '//*[@id="shopping_cart_container"]/a'
           self.remove_id = 'remove-sauce-labs-backpack'
           self.hamburger_id = 'react-burger-menu-btn'
           self.logout_id = 'logout_sidebar_link'

       def username(self, uname):
           self.driver.find_element(By.ID, self.username_id).send_keys(uname)


       def password(self, pas):
           self.driver.find_element(By.ID, self.password_id).send_keys(pas)

       def lon(self):
           self.btn = self.driver.find_element(By.ID, self.lon_id)
           self.driver.execute_script("arguments[0].click()", self.btn)


       def cart(self):
           self.btn = self.driver.find_element(By.ID, self.cart_id)
           self.driver.execute_script("arguments[0].click()", self.btn)

       def filter(self):
           self.btn = self.driver.find_element(By.XPATH, self.filter_XPATH)
           self.driver.execute_script("arguments[0].click()", self.btn)

       def remove(self):
           self.btn = self.driver.find_element(By.ID, self.remove_id)
           self.driver.execute_script("arguments[0].click()", self.btn)

       def hamburger(self):
           self.btn = self.driver.find_element(By.ID, self.hamburger_id)
           self.driver.execute_script("arguments[0].click()", self.btn)

       def logout(self):
           self.btn = self.driver.find_element(By.ID, self.logout_id)
           self.driver.execute_script("arguments[0].click()", self.btn)

