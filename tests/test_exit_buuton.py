from selenium.webdriver.common.by import By
from locators import StellarburgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestStellarburgersLogin:

    def test_exit(self, driver):

        driver.find_element(*StellarburgersLocators.LOGIN_BUTTON_MAIN).click()

        driver.find_element(*StellarburgersLocators.EMAIL_BUTTON) . send_keys("kutepov@gmail.com")
        driver.find_element(*StellarburgersLocators.PASSWORD_BUTTON).send_keys("123456")

        driver.find_element(*StellarburgersLocators.LOGIN_BUTTON).click()


        driver.find_element(*StellarburgersLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((StellarburgersLocators.EXIT_BUTTON)))

        driver.find_element(*StellarburgersLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((StellarburgersLocators.LOGIN_TITEL_MAIN)))

        assert driver.find_element(*StellarburgersLocators.LOGIN_TITEL_MAIN).text == "Вход"