import types
import typing
from selenium import webdriver
import booking.constants as cons
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 
import os
from selenium.webdriver.common.keys import Keys as keys
from booking.booking_filteration import booking_filter 
import time 
from booking.booking_report import booking_report
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from prettytable import PrettyTable 

class booking(webdriver.Chrome):

     def __init__(self,driver_path=r"C:\Users\kaifk\lpth\selenium",teardown=False):
          self.teardown=teardown
          self.driver_path=driver_path
          os.environ['PATH']+=self.driver_path
          # options=webdriver.ChromeOptions()
          # options.add_experimental_option('excludeswitches',['enable-logging'])

          super(booking,self).__init__()
          self.implicitly_wait(15)
          self.maximize_window()

     def __exit__(self, exc_type, exc_val, exc_tb):
          if(self.teardown):
               self.quit()

     def land_first_page(self):
          self.get(cons.base_url)

     def cross_check(self):
               try: 
                    wait=WebDriverWait(self,15)
                    condition = ec.visibility_of_element_located((By.CSS_SELECTOR,'button[aria-label="Dismiss sign-in info."]'))
                    btn=wait.until(condition)
                    btn.click()
               except Exception as e :
                    time.sleep(0.2)
                     
                     
               
               


     def change_currency(self,currency=None):
               wait=WebDriverWait(self,15)
               # condition2 = ec.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-testid="' + str('header-currency-picker-trigger') + '"]'))
               condition2 = ec.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]'))
               currency_btn=wait.until(condition2)
               currency_btn.click()

               selected_item=ec.visibility_of_element_located((By.CSS_SELECTOR,'button[class="fc63351294 ea925ef36a bf97d4018a ae8177da1f cddb75f1fd"]'))
               selected_item_btn=wait.until(selected_item)
               selected_item_btn.click()
     def select_searchbar(self,place_to_go):
          search_field=self.find_element(By.ID,":Ra9:")
          search_field.clear()
          time.sleep(0.5)
          search_field.send_keys(place_to_go)
          time.sleep(2)
          search_field.send_keys(keys.ENTER)
     def enter_dates(self,checkin,checkout):
          wait=WebDriverWait(self,15)
          condition2 = ec.visibility_of_element_located((By.CSS_SELECTOR, f'span[data-date="{checkin}"]'))
          checkin_date=wait.until(condition2)
          checkin_date.click()
          condition2 = ec.visibility_of_element_located((By.CSS_SELECTOR, f'span[data-date="{checkout}"]'))
          checkout_data=wait.until(condition2)
          checkout_data.click()
     def booking_count_inc(self,adult,child=None,rooms=None):
          wait=WebDriverWait(self,10)
          selector=self.find_element(By.CSS_SELECTOR,'button[data-testid="occupancy-config"]')
          selector.click()
          time.sleep(1)
          div_element = self.find_element(By.CLASS_NAME,"e98c626f34")  # Find the <div> element by class name
          adult_btn = div_element.find_element(By.CSS_SELECTOR,"button.fc63351294.a822bdf511.e3c025e003.fa565176a8.f7db01295e.c334e6f658.e1b7cfea84.d64a4ea64d")  # Find the button within the <div> using CSS selector
          
          if(adult==1):
               adult_btn = div_element.find_element(By.CSS_SELECTOR,'button[class="fc63351294 a822bdf511 e3c025e003 fa565176a8 f7db01295e c334e6f658 e1b7cfea84 cd7aa7c891"]')  # Find the button within the <div> using CSS selector
               adult_btn.click()

          if(adult==2):
               print("guests added successfully")
          else:
               while(adult-2):
                    adult_btn.click()
                    time.sleep(0.02)
                    adult-=1
               print("guests added successfully")
          # outer_div=self.find_element(By.CLASS_NAME , 'df856d97eb')
          # print(outer_div)


          

     def click_search(self):
          search_icon=self.find_element(By.CSS_SELECTOR,"button[class='fc63351294 a822bdf511 d4b6b7a9e7 cfb238afa1 c938084447 f4605622ad aa11d0d5cd']")
          search_icon.click()

     def apply_filtration(self):
           filteration=booking_filter(driver=self)
           filteration.apply_star(4,5)
           filteration.sort_low_to_high()

     def report_results(self):
           boxes=self.find_element(By.ID,"search_results_table")
           report=booking_report(boxes)
           table=PrettyTable(
                 field_names=["Hotel Name", "Price per night","Star Rating"]
                 
                 )
           table.add_rows(report.pull_attributes())
           print(table)
           
           

   
    






