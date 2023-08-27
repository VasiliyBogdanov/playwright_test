from playwright.sync_api import Page


class BasePage:
    def __init__(self,
                 page: Page,
                 initial_address: str):
        self.page = page
        self._initial_address = initial_address
        self.page.goto(self._initial_address)

    @property
    def get_initial_address(self):
        return self._initial_address
