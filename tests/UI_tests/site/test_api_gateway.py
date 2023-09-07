from playwright.sync_api import Page

from framework.pages.MainPage import MainPage


class TestAPIGatewayUI:
    """Class for UI testing API Gateway"""

    def test_goto_APIGateway(self, page: Page):
        """Go to API Gateway page from main page through Services menu in the
         header"""
        api_gw = "API Gateway"

        main_page = MainPage(page)
        main_page.header.services.click()
        main_page.header.services.sidebar_click(title="Инфраструктура")
        main_page.header.services.grid_elem_click(title=api_gw)

        api_gw_url = main_page.header.services.grid_elems.get(api_gw)
        assert main_page.page.url == api_gw_url, \
            f"Переход на страницу API Gateway по адресу {api_gw_url} не удался"
