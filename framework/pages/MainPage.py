from playwright.sync_api import Page

from framework.Addresses import MAIN_ADDR
from .BasePage import BasePage
from .page_elements.Header import Header


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, MAIN_ADDR)
        self.header = Header(page)
