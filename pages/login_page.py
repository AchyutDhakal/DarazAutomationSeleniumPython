from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    LOGIN_LINK = (By.XPATH, "//a[normalize-space()='Login']")
    USERNAME_INPUT = (By.XPATH, "//input[@placeholder='Please enter your Phone or Email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Please enter your password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='LOGIN']")
    FORGOT_PASSWORD = (By.XPATH, "//div[text()='Forgot password?']")
    SIGNUP_LINK = (By.XPATH, "//span[text()='Sign up']")
    GOOGLE_LOGIN = (By.XPATH, "//span[normalize-space()='Google']")
    PROFILE_ICON = (By.ID,"myAccountTrigger")
    FORGOT_PASSWORD_PHONE_INPUT = (By.XPATH,"//input[@placeholder='Please enter your Phone Number or Email']")
    FORGOT_PASSWORD_CONFIRM_BUTTON = (By.XPATH,"//button[contains(@class,'iweb-button-primary') and not(contains(@class,'disabled'))]")

    FORGOT_PASSWORD_BACK_BUTTON = (By.XPATH, "(//div[@class='iweb-button-mask'])[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_login_link(self):
        self.click_element(self.LOGIN_LINK)

    def enter_username(self, username):
        self.enter_text(username, self.USERNAME_INPUT)

    def enter_password(self, password):
        self.enter_text(password, self.PASSWORD_INPUT)

    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.click_login_link()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def click_forgot_password(self):
        self.click_element(self.FORGOT_PASSWORD)

    def enter_forgot_password_phone_number(self, phone_number):
        self.enter_text(phone_number,self.FORGOT_PASSWORD_PHONE_INPUT)

    def click_forgot_password_confirm_button(self):
        self.click_element(self.FORGOT_PASSWORD_CONFIRM_BUTTON)

    def click_forgot_password_back_button(self):
        self.click_element(self.FORGOT_PASSWORD_BACK_BUTTON)

    def forgot_password(self, phone_number):
        self.click_login_link()
        self.click_forgot_password()
        self.enter_forgot_password_phone_number(phone_number)
        self.click_forgot_password_confirm_button()

    

    