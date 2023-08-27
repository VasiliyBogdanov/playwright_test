from playwright.sync_api import Page

from framework.pages.MainPage import MainPage
from framework.pages.page_elements.Services import API_GATEWAY_ADDR


class TestAPIGatewayUI:
    """Class for UI testing API Gateway"""

    def test_goto_APIGateway(self, page: Page):
        """Go to API Gateway page from main page through Services menu in the
         header"""

        mainpage = MainPage(page)
        mainpage.header.services.click()
        mainpage.header.services.sidebar_click("Инфраструктура")
        mainpage.header.services.grid_elem_click("API Gateway")

        assert page.url == API_GATEWAY_ADDR
