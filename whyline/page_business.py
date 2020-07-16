from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PageBusiness():
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_button = (By.XPATH, '//*[@id="top-enterprise"]/div[2]/p[3]/a')

    def enter_sign_in_button(self):
        try:
            button_sign_in = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.sign_in_button))
            button_sign_in.click()
        except:
            print("No se encuentra 'sign_in_button'.")