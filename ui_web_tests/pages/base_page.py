import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from ui_web_tests.utilities.useful_func import get_base_url

class BasePage(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def element(self, locator, timeout=3):
        # return self.driver.find_element(*locator)
        return WebDriverWait(self.driver, timeout=timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Navigate to main page')
    def navigate_to_main(self):
        self.driver.get(get_base_url())

    def is_element_not_displayed(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout=timeout).until(EC.visibility_of_element_located(locator))
            is_not_displayed = False
        except TimeoutException:
            is_not_displayed = True
        return is_not_displayed

