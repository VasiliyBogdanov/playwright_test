from playwright.sync_api import Page

from .BasePage import BasePage
from .page_elements.Header import Header


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, "https://cloud.ru/ru")
        self.header = Header(page)
