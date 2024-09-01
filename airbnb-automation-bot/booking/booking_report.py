from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BookingReport:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def pull_attributes(self):
        collection = []
        wait = WebDriverWait(self.driver, 20)

        try:
            wait.until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, 
            'div[class="g1qv1ctd atm_u80d3j_1li1fea atm_c8_o7aogt atm_g3_8jkm7i c1v0rf5q atm_9s_11p5wf0 atm_cx_4wguik atm_dz_7esijk atm_e0_1lo05zz dir dir-ltr"]')) >= 18)

            deals = self.driver.find_elements(By.CSS_SELECTOR, 'div[class="g1qv1ctd atm_u80d3j_1li1fea atm_c8_o7aogt atm_g3_8jkm7i c1v0rf5q atm_9s_11p5wf0 atm_cx_4wguik atm_dz_7esijk atm_e0_1lo05zz dir dir-ltr"]')

            for deal in deals:
                deal_name = deal.find_element(By.CSS_SELECTOR, 'div[data-testid="listing-card-title"]').get_attribute('innerHTML').strip()
                deal_desc = deal.find_element(By.CSS_SELECTOR, 'span[data-testid="listing-card-name"]').get_attribute('innerHTML').strip()
                deal_price = deal.find_element(By.CSS_SELECTOR, 'span[class="_11jcbg2"]').get_attribute('innerHTML').strip().replace('&nbsp;', ' ')
                outer_span_rating = deal.find_element(By.CSS_SELECTOR, 'span.r4a59j5')
                deal_rating = outer_span_rating.find_element(By.CSS_SELECTOR, 'span[aria-hidden="true"]').get_attribute('innerHTML').strip()
                collection.append([deal_name, deal_desc, deal_price, deal_rating])

        except Exception as e:
            print(f"Error locating the deals: {e}")

        return collection