import pytest
from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()

        # send the driver as an argument to the HomePage class
        homePage = HomePage(self.driver)
        checkOutPage = homePage.shopItems()

        log.info("getting all the card titles")
        products = checkOutPage.getProductTitles()

        i = -1
        for product in products:
            i = i + 1
            product_name = product.text
            log.info(product_name)
            if product_name == "Blackberry":
                # Add item into cart
                checkOutPage.getProductButtons()[i].click()

        checkOutPage.getCheckoutButton().click()
        confirmPage = checkOutPage.getCheckoutButton2()
        log.info("Entering country name as ind")
        self.driver.find_element(By.ID, "country").send_keys("ind")


        self.verifyLinkPresence("India")
        #self.driver.find_element(By.LINK_TEXT, "India").click()
        confirmPage.selectIndia().click()


        confirmPage.confirmCheckbox().click()
        confirmPage.purchaseProducts().click()
        success_message = self.driver.find_element(By.XPATH, "//div[@class = 'alert alert-success alert-dismissible']").text
        log.info("Text received from application is " + success_message)
        assert "gddasd" in success_message

        self.driver.get_screenshot_as_file("screen.png")
