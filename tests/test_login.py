import pytest
from data.test_data import VALID_DATA, INVALID_DATA, PHONE_NUMBER_FORGOT_PASSWORD
from utils.test_runner import create_driver
from pages.login_page import LoginPage
import time
from utils.assertions import assert_true, assert_false

class TestLogin():
    def setup_method(self):
        self.driver = create_driver()
        self.driver.get("https://www.daraz.com.np/#?")

        self.login_page = LoginPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("valid_data",VALID_DATA)
    def test_valid_login(self,valid_data):
        self.login_page.login(valid_data['username'], valid_data['password'])
        time.sleep(5)

        assert_true(self.login_page.is_element_visible(self.login_page.PROFILE_ICON), "Profile icon is not visible so login unsuccessful")

    @pytest.mark.parametrize("invalid_data",INVALID_DATA)
    def test_invalid_login(self,invalid_data):     
        self.login_page.login(invalid_data['username'], invalid_data['password'])
        time.sleep(5)

        assert_false(self.login_page.is_element_visible(self.login_page.PROFILE_ICON), "Profile icon visible whichshould not be visible")

    @pytest.mark.parametrize("phone_number", PHONE_NUMBER_FORGOT_PASSWORD)        
    def test_forgot_password(self, phone_number):
        self.login_page.forgot_password(phone_number['phone_number'])
        time.sleep(5)

        assert_false(self.login_page.is_element_visible(self.login_page.PROFILE_ICON), "Profile icon visible whichshould not be visible after forgot password")

    

