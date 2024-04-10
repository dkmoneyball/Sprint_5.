from selenium.webdriver.common.by import By
from locators import StellarburgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestStellarburgersLogin:

    def test_login(self, driver):

        driver.find_element(*StellarburgersLocators.LOGIN_BUTTON_MAIN).click()

        driver.find_element(By.XPATH, "//input[@name = 'name' ]") . send_keys("kutepov@gmail.com")
        driver.find_element(By.XPATH, "//input[@type= 'password' and @name='Пароль']").send_keys("123456")

        driver.find_element(By.XPATH, "//button[text()='Войти']").click()


        driver.find_element(*StellarburgersLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((StellarburgersLocators.STELLAR_BURGER_BUTTON)))

        driver.find_element(*StellarburgersLocators.STELLAR_BURGER_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((StellarburgersLocators.GET_ORDER_BUTTON)))

        assert driver.find_element(*StellarburgersLocators.GET_ORDER_BUTTON).is_displayed()