from selenium.webdriver.common.by import By

class StellarburgersLocators:
    # Кнопка войти в аккаунт
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text() = 'Войти в аккаунт']")
    # Название Вход
    LOGIN_TITEL_MAIN = (By.XPATH, "//h2[text() = 'Вход']")
    # Кнопка регистрации на главной транице
    REGISTER_BUTTON_ON_LOGIN_PAGE = (By.XPATH, "//a[@class='Auth_link__1fOlj' and contains(@href, '/register')]")

    # Кнопка зарегестрироваться
    REGISTRATION_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Зарегистрироваться']")
    # Поле ввода имени
    REGISTRATION_NAME = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input")
    # Поле ввода пароля
    REGISTRATION_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input")
    # Поле ввода email
    REGISTRATION_EMAIL = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")
    # Кнопка получить заказ
    GET_ORDER_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']")
    # Надпись Некорректний пароль при вводе неправильного пароля
    INCORRECT_PASSWORD_NOTIFY = (By.XPATH, "//p[text()='Некорректный пароль']")
    # Кнопка личный кабинет
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    # Кнопка Войти в разделе Личный кабинет
    LOGIN_BUTTON_ON_REGISTRATION_PAGE = (By.XPATH, "//a[text()='Войти']")
    # Кнопка Профиль в разделе Личный кабинет
    PROFILE_BUTTON_ON_PERSONAL_ACCOUNT = (By.XPATH, "//a[text() = 'Профиль']")
    # Кнопка контсруктор
    COSTRUCTION_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    # Кнопка Stellar Burger
    STELLAR_BURGER_BUTTON = (By.XPATH, "//*[@id='root']/div/header/nav/div/a")
    # Кнопка Булки
    BULKI_BUTTON = (By.XPATH, "//span[text()='Булки']")
    # Кнопка Краторная булка
    KRATORNAY_BULKA_BUTTON = (By.XPATH, "//p[text()='Краторная булка N-200i']")
    # Кнопка Соусы
    SAUCES_BUTTON = (By.XPATH, "//span[text()='Соусы']")
    # Кнопка Соус фирменый
    SPETIAL_SAUCES_BUTTON = (By.XPATH, "//p[text()='Соус фирменный Space Sauce']")
    # Кнопка Начинки
    FILLING_BUTTON = (By.XPATH, "//span[text()='Начинки']")
    # Кнопка Говяжий метиорит
    METIOR_FILLING_BUTTON = (By.XPATH, "//p[text()='Говяжий метеорит (отбивная)']")
    # Кнопка Выход
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")

