from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")


class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    LOGIN_EMAIL_FIELD = (By.XPATH, "//input[@name='login-username']")
    LOGIN_PASSWORD_FIELD = (By.XPATH, "//input[@name='login-password']")
    REGISTRATION_FORM = (By.XPATH, "//form[@id='register_form']")
    REGISTRATION_EMAIL_FIELD = (By.XPATH, "//input[@name='registration-email']")
    REGISTRATION_EMAIL_PASSWORD = (By.XPATH, "//input[@name='registration-password1']")
    REGISTRATION_EMAIL_PASSWORD_REFRESH = (By.XPATH, "//input[@name='registration-password2']")
