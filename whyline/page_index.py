from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PageIndex():
    def __init__(self, driver):
        self.driver = driver
        self.lenguaje_button = (By.XPATH, '/html/body/vex-root/vex-custom-layout/vex-layout/div/mat-sidenav-container/mat-sidenav-content/vex-toolbar/div/div/div[2]/div/button')
        self.eeuu_button = (By.XPATH, '//*[@id="mat-menu-panel-0"]/div/button[1]')
        self.brasil_button = (By.XPATH, '//*[@id="mat-menu-panel-0"]/div/button[3]')
        self.subtitle = (By.XPATH, '//*[@id="hero"]/div/div[1]/h2')
        self.business_button = (By.XPATH, '/html/body/vex-root/vex-custom-layout/vex-layout/div/mat-sidenav-container/mat-sidenav-content/vex-toolbar/div/div/div[1]/vex-navigation-item[1]/a')

    def enter_lenguaje_button(self):
        try:
            button_lenguaje = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.lenguaje_button))
            button_lenguaje.click()
        except:
            print("No se encuentra 'lenguaje_button'.")

    def enter_eeuu_button(self):
        try:
            button_eeuu = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.eeuu_button))
            button_eeuu.click()
        except:
            print("No se encuentra 'eeuu_button'.")

    def enter_brasil_button(self):
        try:
            button_brasil = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.brasil_button))
            button_brasil.click()
        except:
            print("No se encuentra 'brasil_button'.")

    def return_subtitle_text(self):
        try:
            text_subtitle = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.subtitle))
            return text_subtitle.text
        except:
            print("No se encuentra 'subtitle'.")

    def enter_business_button(self):
        try:
            button_business = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.business_button))
            button_business.click()
        except:
            print("No se encuentra 'business_button'.")