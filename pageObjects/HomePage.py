from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    #create a constructor that will accept the driver as an argument
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[@href='/angularpractice/shop']")
    name = (By.CSS_SELECTOR, "[name='name'")
    email = (By.NAME, "email")
    icecream = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    success_message = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItems(self):
        # use * if you use tuple
        # self.driver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']")
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckoutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def checkIcecream(self):
        return self.driver.find_element(*HomePage.icecream)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.success_message)
