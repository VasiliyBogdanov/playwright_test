from playwright.sync_api import Page

from .BaseElement import BaseElement
from .Services import Services


class Header(BaseElement):
    def __init__(self, page: Page):
        super().__init__(page)
        self.services = Services(page)
