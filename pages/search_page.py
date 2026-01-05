from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):
    SEARCH_BOX = (By.XPATH,"//input[@type='search']")
    SEARCH_BUTTON = (By.XPATH,"//a[@class='search-box__button--1oH7']")
    SEARCHED_PRODUCT = (By.XPATH,"//h1[@class='JrAyI']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_search_keyword(self, keyword):
        self.enter_text(keyword, self.SEARCH_BOX)

    def click_search_button(self):
        self.click_element(self.SEARCH_BUTTON)

    def search(self,keyword):
        self.enter_search_keyword(keyword)
        self.click_search_button()

    
