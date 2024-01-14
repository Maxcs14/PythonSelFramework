from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    # create a constructor that will accept the driver as an argument
    def __init__(self, driver):
        self.driver = driver

    # card Title
    productTitles = (By.CSS_SELECTOR, ".card-title a")
    # card Footer
    productButtons = (By.CSS_SELECTOR, ".card-footer button")
    #
    checkoutButton = (By.PARTIAL_LINK_TEXT, "Checkout")
    checkoutButton2 = (By.XPATH, "//button[@class='btn btn-success']")

    def getProductTitles(self):
        # products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        return self.driver.find_elements(*CheckoutPage.productTitles)

    def getProductButtons(self):
        # product.find_element(By.XPATH, "div/button").click()
        return self.driver.find_elements(*CheckoutPage.productButtons)

    def getCheckoutButton(self):
        # self.driver.find_element(By.PARTIAL_LINK_TEXT, "Checkout").click()
        return self.driver.find_element(*CheckoutPage.checkoutButton)

    def getCheckoutButton2(self):
        self.driver.find_element(*CheckoutPage.checkoutButton2).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage