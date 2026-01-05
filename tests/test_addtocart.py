import pytest
import time
from pages.search_page import SearchPage
from pages.login_page import LoginPage
from pages.add_to_cart_page import AddToCartPage
from utils.test_runner import create_driver
from data.test_data import VALID_DATA, SEARCH_KEYWORDS
from utils.assertions import assert_true

class TestAddToCart():
    def setup_method(self):
        self.driver = create_driver()
        self.driver.get("https://www.daraz.com.np/#?")

        self.search_page = SearchPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.add_to_cart_page = AddToCartPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("valid_data",VALID_DATA)
    @pytest.mark.parametrize("keyword", SEARCH_KEYWORDS)
    def test_add_to_cart(self,keyword, valid_data):
        self.login_page.login(valid_data['username'], valid_data['password'])
        time.sleep(5)
        self.search_page.search(keyword['keyword'])
        self.add_to_cart_page.click_product()
        
        self.add_to_cart_page.click_add_to_cart_button()
        self.add_to_cart_page.click_cross_icon()
        self.add_to_cart_page.click_cart_icon()

        cart_product = self.add_to_cart_page.get_element_text(self.add_to_cart_page.CART_PRODUCT).lower()

        time.sleep(3)

        assert_true(keyword['keyword'].lower() in cart_product, "The product clicked does not match the product on the cart")



