import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_index import PageIndex
from page_business import PageBusiness
from sign_in_page import SignInPage

class WhyLine (unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument("start-maximized")
        self.driver = webdriver.Chrome('chromedriver.exe', chrome_options=option)
        self.driver.get('https://www.whyline.com/home/')
        self.indexPage = PageIndex(self.driver)
        self.businessPage = PageBusiness(self.driver)
        self.signInPage = SignInPage(self.driver)

    def test_lenguaje_eeuu(self):
        try:
            self.indexPage.enter_lenguaje_button()
            self.indexPage.enter_eeuu_button()
            self.assertIn('Optimize Time & Cut Costs.', self.indexPage.return_subtitle_text())
            self.indexPage.enter_lenguaje_button()
            self.indexPage.enter_brasil_button()
            self.assertIn('Otimize seu tempo e corte custos.', self.indexPage.return_subtitle_text())
        except:
            self.driver.save_screenshot("error_test_lenguaje.jpg")

    def test_sign_in(self):
        try:
            self.indexPage.enter_business_button()
            self.businessPage.enter_sign_in_button()
            self.signInPage.complete_textbox_email('hola@gmail.com.ar')
            self.signInPage.complete_textbox_pass('12345')
            self.signInPage.enter_send_button()
            self.assertIn('El captcha es obligatorio', self.signInPage.return_error_message())
        except:
            self.driver.save_screenshot("error_test_sign_in.jpg")



    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if  __name__ == '__main__':
    unittest.main()