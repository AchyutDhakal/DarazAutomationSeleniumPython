from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AddToCartPage(BasePage):
    PRODUCT = (By.XPATH,"//div[@class='ant-col ant-col-20 ant-col-push-4 Jv5R8 css-1bkhbmc app']//div[1]//div[1]//div[1]//div[2]//div[2]//a[1]")
    PRODUCT_NAME = (By.XPATH,"//h1[@class='pdp-mod-product-badge-title']")
    ADD_TO_CART_BUTTON = (By.XPATH,"//button[contains(@class,'pdp-button pdp-button_type_text pdp-button_theme_orange pdp-button_size_xl')]")
    CROSS_ICON = (By.XPATH,"//i[contains(@class,'next-icon next-icon-close next-icon-small')]")
    CART_ICON = (By.XPATH,"//span[contains(@class,'cart-icon-daraz')]//*[name()='svg']")
    CART_PRODUCT = (By.XPATH,"//a[contains(@class,'automation-link-from-title-to-prod')]")

    def __init__(self,driver):
        super().__init__(driver)

    def click_product(self):
        self.click_element(self.PRODUCT)

    def click_add_to_cart_button(self):
        self.click_element(self.ADD_TO_CART_BUTTON)

    def click_cross_icon(self):
        self.click_element(self.CROSS_ICON)

    def click_cart_icon(self):
        self.click_element(self.CART_ICON)

        