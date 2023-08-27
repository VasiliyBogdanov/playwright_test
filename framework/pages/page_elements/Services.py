import re

from playwright.sync_api import Page

from .BaseElement import BaseElement

API_GATEWAY_ADDR = "https://cloud.ru/ru/products/oblachnyj-api-gateway-hosting"


class Services(BaseElement):
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
        self.page.wait_for_url(API_GATEWAY_ADDR)
