import re

from playwright.sync_api import Page

from framework.Addresses import MAIN_ADDR, PATHS
from .BaseElement import BaseElement


class Services(BaseElement):
    grid_elems = {
        "API Gateway": "".join([MAIN_ADDR, PATHS["API Gateway"]])
    }

    def __init__(self, page: Page):
        super().__init__(page)

    def click(self):
        self.page.get_by_role("navigation").get_by_text("Сервисы") \
            .click()

    def sidebar_click(self, title: str):
        self.page.locator("#portal div") \
            .filter(has_text=re.compile(f"^{title}$")) \
            .click()

    def grid_elem_click(self, title: str):
        self.page.get_by_role("link", name=title) \
            .first.click()
        self.page.wait_for_url(self.grid_elems[title])
