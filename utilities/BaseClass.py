import inspect
import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        # create the logger object
        logger = logging.getLogger(loggerName)
        # create the Filehandler location file
        fileHandler = logging.FileHandler("logfile.log")
        # create a format for the filehandler
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        # set the format of the filehandler
        fileHandler.setFormatter(formatter)

        # add the filehandler
        logger.addHandler(fileHandler)  # filehandler object
        # set level of logging
        logger.setLevel(logging.DEBUG)
        return logger