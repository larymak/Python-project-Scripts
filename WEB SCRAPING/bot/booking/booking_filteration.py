from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time
class booking_filter:
    def __init__(self,driver:WebDriver):
        self.driver=driver

        
        

    def apply_star(self,*stars):
        box=self.driver.find_element(By.CSS_SELECTOR,"div[data-filters-group='class']")
        star_child_elements=box.find_elements(By.CSS_SELECTOR,"*")
        for s in stars:
            time.sleep(0.2)
            for i in star_child_elements:
                if str(i.get_attribute('innerHTML')).strip()  == f'{s} stars':
                    i.click()
    def sort_low_to_high(self):
        low_price = self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="sorters-dropdown-trigger"]')
        low_price.click()
        wait=WebDriverWait(self.driver,10)

        condition=ec.visibility_of_element_located((By.CSS_SELECTOR,'button[data-id="class"]'))      
        btn_sort=wait.until(condition)  
        btn_sort.click()

