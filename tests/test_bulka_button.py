from selenium.webdriver.common.by import By
from locators import StellarburgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestStellarburgersLogin:

    def test_login(self, driver):



        driver.find_element(*StellarburgersLocators.SAUCES_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((StellarburgersLocators.BULKI_BUTTON)))

        driver.find_element(*StellarburgersLocators.BULKI_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((StellarburgersLocators.KRATORNAY_BULKA_BUTTON)))




        assert driver.find_element(*StellarburgersLocators.KRATORNAY_BULKA_BUTTON).is_displayed()