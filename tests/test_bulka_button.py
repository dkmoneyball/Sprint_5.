from selenium.webdriver.common.by import By
from locators import StellarburgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestStellarburgersLogin:

    def test_bulka_button(self, driver):
        driver.find_element(*StellarburgersLocators.SAUCES_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (StellarburgersLocators.BULKI_BUTTON)))

        driver.find_element(*StellarburgersLocators.BULKI_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                (StellarburgersLocators.BULKI_BUTTON_ON_FOCUS)))

        assert driver.find_element(
            *StellarburgersLocators.BULKI_BUTTON_ON_FOCUS).is_displayed()
