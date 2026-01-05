import pytest
import time
from pages.search_page import SearchPage
from utils.test_runner import create_driver
from data.test_data import SEARCH_KEYWORDS
from utils.assertions import assert_true

class TestSearch():
    def setup_method(self):
        self.driver = create_driver()
        self.driver.get("https://www.daraz.com.np/#?")

        self.search_page = SearchPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("keyword",SEARCH_KEYWORDS)
    def test_valid_search(self, keyword):
        self.search_page.search(keyword['keyword'])

        actual_text = self.search_page.get_element_text(self.search_page.SEARCHED_PRODUCT)
        time.sleep(3)
                
        assert_true(keyword['keyword'].lower() in actual_text.lower(),"Searched product did not match")

