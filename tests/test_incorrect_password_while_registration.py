from selenium.webdriver.common.by import By
import settings
from locators import StellarburgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestStellarburgersIncorrectPasswordWhileRegistration:

    def test_incorrect_password_while_registration(self, driver):
        driver.get(settings.URL + "register")


        driver.find_element(*StellarburgersLocators.REGISTRATION_NAME).send_keys("Даниил")
        driver.find_element(*StellarburgersLocators.REGISTRATION_EMAIL).send_keys("kutepov@gmail.com")
        driver.find_element(*StellarburgersLocators.REGISTRATION_PASSWORD).send_keys("12345")
        driver.find_element(*StellarburgersLocators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellarburgersLocators.INCORRECT_PASSWORD_NOTIFY)))

        assert driver.find_element(*StellarburgersLocators.INCORRECT_PASSWORD_NOTIFY).text == "Некорректный пароль"