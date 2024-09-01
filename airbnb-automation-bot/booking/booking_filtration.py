from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver
    
    def select_filters(self, max_price, num_people):
        filter_btn = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="category-bar-filter-button"]')
        filter_btn.click()
        # filter by maximum price 
        price_field = self.driver.find_element(By.ID, 'price_filter_max')
        price_field.send_keys(Keys.BACKSPACE * len(price_field.get_attribute('value')))
        price_field.send_keys(max_price)
        # select number of bedrooms and beds based on number of people going
        bedroom_increase = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="stepper-filter-item-min_bedrooms-stepper-increase-button"]')
        bed_increase = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="stepper-filter-item-min_beds-stepper-increase-button"]')
        for i in range(num_people):
            bedroom_increase.click()
            bed_increase.click()
        # select free parking amenity
        free_parking = self.driver.find_element(By.ID, 'filter-item-amenities-9')
        free_parking.click()
        # click the apply button
        parent = self.driver.find_element(By.CSS_SELECTOR, 'div[class="ptiimno atm_7l_1p8m8iw dir dir-ltr"]')
        apply_filters = parent.find_element(By.CSS_SELECTOR, '*')
        apply_filters.click()




        