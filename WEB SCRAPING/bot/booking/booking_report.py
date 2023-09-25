#file is going to include methods that will parse 
# the specific data that we need from each boxes 
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

class booking_report:
    def __init__(self,boxes_sec:WebElement) -> None:
        self.boxes_sec=boxes_sec
        self.hotel_names=self.pull_deal_boxes()

    def pull_deal_boxes(self):
         return self.boxes_sec.find_elements(By.CLASS_NAME,"a826ba81c4")
    

    def pull_attributes(self):
          collections=[]
          try:
               if len(self.hotel_names) > 0:
                    for i in self.hotel_names:
                         try:
                              hotel_name_element = i.find_element(By.CSS_SELECTOR,"[data-testid='title']")
                              hotel_name = hotel_name_element.get_attribute('innerHTML').strip()

                              hotel_price=i.find_element(By.CSS_SELECTOR,"span[data-testid='price-and-discounted-price']").get_attribute('innerHTML').strip()
                              score_element = i.find_element(By.CSS_SELECTOR, "div[data-testid='review-score'] div[class='b5cd09854e d10a6220b4']")
                              collections.append([hotel_name,hotel_price,score_element.text])

                              

                         except StaleElementReferenceException:
                              print("Stale element reference exception occurred while retrieving hotel name.")
                         except NoSuchElementException:
                              print("Hotel name element not found for this item.")
               else:
                    collections.append([None,None,None])
          except StaleElementReferenceException:
               self.refresh()
               
          return collections

