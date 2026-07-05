from playwright.sync_api import Page, sync_playwright

class LoginPage:

    def __init__(self,page:Page):
        self.page = page

    def go_to_login_page(self,page):
        self._navigate_site=page.goto("https://practicetestautomation.com/practice-test-login/")
        self._username=page.locator("#username")
        self._password=page.locator("#password")
        self.login=page.locator("#submit")

    def credential(self,page):
        self.u_name=self._username.fill("student")
        self.p_word=self._password.fill("Password123")
        self.login.click()



