import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable 

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:/Program Files (x86)/chromedriver.exe"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        input("Press enter to close browser")
        self.quit()

    def load_first_page(self):
        self.get(const.AIRBNB)
        # click ok to get rid of cookies message
        ok_btn = self.find_element(By.XPATH, "//button[contains(text(), 'OK')]")
        ok_btn.click()

    def search_location(self, location=None):
        search_field = self.find_element(By.CSS_SELECTOR, 'input[placeholder="Search destinations"]')
        search_field.clear()
        search_field.send_keys(location)
        # wait until an element with text appears in the dropdown
        WebDriverWait(self, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, f"//*[contains(text(), '{location}')]"), location)
        )
        first_result = self.find_element(By.CSS_SELECTOR, 'div[data-index="0"]')
        first_result.click()
    
    def select_dates(self, check_in, check_out):
        try:
            # Try to find and click the first element
            check_in_element = self.find_element(By.CSS_SELECTOR, f'div[data-testid="{check_in}"]')
            check_in_element.click()
            check_out_element = self.find_element(By.CSS_SELECTOR, f'div[data-testid="{check_out}"]')
            check_out_element.click()
        except Exception as e:
            # If the first action fails, catch the exception and try the second action
            check_in_element = self.find_element(By.CSS_SELECTOR, f'div[data-testid="calendar-day-{check_in}"]')
            check_in_element.click()
            check_out_element = self.find_element(By.CSS_SELECTOR, f'div[data-testid="calendar-day-{check_out}"]')
            check_out_element.click()
    
    def select_guests(self, adult_count, child_count):
        selection_element = self.find_element(By.XPATH, "//div[contains(text(), 'Who')]")
        selection_element.click()
        # increase number of adults
        adult_increase = self.find_element(By.CSS_SELECTOR, 'button[data-testid="stepper-adults-increase-button"]')
        for i in range(adult_count):
            adult_increase.click()
        # increase number of children
        child_increase = self.find_element(By.CSS_SELECTOR, 'button[data-testid="stepper-children-increase-button"]')
        for i in range(child_count):
            child_increase.click()
            
    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR, 'button[data-testid="structured-search-input-search-button"]')
        search_button.click()

    def apply_filters(self, max_price, num_people):
        filtration = BookingFiltration(driver=self)
        filtration.select_filters(max_price, num_people)
        
    def report_results(self):
        report = BookingReport(driver=self)
        
        table = PrettyTable(
            field_names=["Name", "Description", "Price", "Rating"]
        )
        table.add_rows(report.pull_attributes())
        print(table)