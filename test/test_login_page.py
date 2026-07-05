import playwright
import pytest
from Page.Login_Page import LoginPage
from playwright.sync_api import Page, expect, sync_playwright, Playwright

from confitest.Preinstall import browser_launch
def browser_launch_launch(page):
      browser=browser_launch(page)
      return browser

 def test_login_page(page:Page):

    login_page = LoginPage(page)
    login_page.go_to_login_page(page)
    login_page.credential(page)
    page.wait_for_timeout(5000)

    #expect(".post-title").to_be_visible("Logged In Successfully")
    #expect(".post-title").to_have_text("Logged In Successfully")
    #page.wait_for_timeout(5000)