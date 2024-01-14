from selenium.webdriver.common.by import By

class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    india = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    clickPurchase = (By.CSS_SELECTOR, "input[value= 'Purchase']")

    def selectIndia(self):
        return self.driver.find_element(*ConfirmPage.india)

    def confirmCheckbox(self):
        # self.driver.find_element(*ConfirmPage.confirmCheckbox)
        return self.driver.find_element(*ConfirmPage.checkbox)

    def purchaseProducts(self):
        # self.driver.find_element(By.CSS_SELECTOR, "input[value= 'Purchase']").click()
        return self.driver.find_element(*ConfirmPage.clickPurchase)



