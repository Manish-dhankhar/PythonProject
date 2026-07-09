import playwright
import pytest
from Page.Login_Page import LoginPage
from playwright.sync_api import Page, expect, sync_playwright, Playwright


def test_login_page(page:Page):

    login_page = LoginPage(page)
    login_page.go_to_login_page(page)
    login_page.credential(page)
    page.wait_for_timeout(2000)


    #expect(page.get_by_text("Logged In Successfully")).to_have_text("Logged In Successfully")
    expect(page.get_by_text("Logged In Successfully")).to_be_visible()
    page.wait_for_timeout(2000)