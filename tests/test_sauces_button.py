from selenium.webdriver.common.by import By
from locators import StellarburgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestStellarburgersLogin:

    def test_login(self, driver):



        driver.find_element(*StellarburgersLocators.SAUCES_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((StellarburgersLocators.SPETIAL_SAUCES_BUTTON)))




        assert driver.find_element(*StellarburgersLocators.SPETIAL_SAUCES_BUTTON).is_displayed()
