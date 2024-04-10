from selenium.webdriver.common.by import By

import settings
from locators import StellarburgersLocators


class TestStellarburgersRegistration:

    def test_registration(self, driver):
        driver.get(settings.URL + "register")


        driver.find_element(*StellarburgersLocators.REGISTRATION_NAME).send_keys("Даниил")
        driver.find_element(*StellarburgersLocators.REGISTRATION_EMAIL).send_keys("kutepov@gmail.com")
        driver.find_element(*StellarburgersLocators.REGISTRATION_PASSWORD).send_keys("123456")

        driver.find_element(*StellarburgersLocators.REGISTRATION_BUTTON).click()


