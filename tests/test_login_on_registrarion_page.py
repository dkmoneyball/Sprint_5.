
from selenium.webdriver.common.by import By
import settings
from locators import StellarburgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestStellarburgersLoginOnRegistrarionPage:

    def test_registration(self, driver):
        driver.get(settings.URL + "register")

        driver.find_element(*StellarburgersLocators.LOGIN_BUTTON_ON_REGISTRATION_PAGE).click()
        driver.find_element(*StellarburgersLocators.EMAIL_BUTTON).send_keys("kutepov@gmail.com")
        driver.find_element(*StellarburgersLocators.PASSWORD_BUTTON).send_keys("123456")

        driver.find_element(*StellarburgersLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((StellarburgersLocators.GET_ORDER_BUTTON)))


        assert driver.find_element(*StellarburgersLocators.GET_ORDER_BUTTON).is_displayed(), "Order button does not exist"