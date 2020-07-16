from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class SignInPage():
    def __init__(self, driver):
        self.driver = driver
        self.textbox_email = (By.XPATH, '//*[@id="sign-in"]/div[1]/div[2]/form/div[1]/label/input')
        self.textbox_pass = (By.XPATH, '//*[@id="sign-in"]/div[1]/div[2]/form/div[2]/label/input')
        self.send_button = (By.XPATH, '//*[@id="sign-in"]/div[1]/div[2]/form/div[4]/button')
        self.error_message = (By.CLASS_NAME, 'toast-message')

    def complete_textbox_email(self, item):
        try:
            email_textbox = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.textbox_email))
            email_textbox.send_keys(item)
        except:
            print("No se encuentra 'textbox_email'.")

    def complete_textbox_pass(self, item):
        try:
            pass_textbox = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.textbox_pass))
            pass_textbox.send_keys(item)
        except:
            print("No se encuentra 'textbox_pass'.")

    def enter_send_button(self):
        try:
            button_send = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.send_button))
            button_send.click()
        except:
            print("No se encuentra 'send_button'.")

    def return_error_message(self):
        try:
            message_error = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.error_message))
            return message_error.text
        except:
            print("No se encuentra 'error_message'.")