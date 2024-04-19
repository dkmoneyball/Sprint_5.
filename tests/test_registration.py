from selenium.webdriver.common.by import By
import settings
from locators import StellarburgersLocators
import random
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestStellarburgersRegistration:

    def test_registration(self, driver):
        driver.get(settings.URL + "register")

        driver.find_element(*StellarburgersLocators.REGISTRATION_NAME).send_keys("Даниил")
        random_number = random.randint(100, 999)
        driver.find_element(*StellarburgersLocators.REGISTRATION_EMAIL).send_keys(f"Vasissualy7{random_number}@ya.ru")
        driver.find_element(*StellarburgersLocators.REGISTRATION_PASSWORD).send_keys("123456")

        driver.find_element(*StellarburgersLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((StellarburgersLocators.LOGIN_TITEL_MAIN)))
        assert driver.find_element(*StellarburgersLocators.LOGIN_TITEL_MAIN).text == "Вход"
