from playwright.sync_api import Page, expect, sync_playwright, Playwright
def browser_launch(page:Page):
 with sync_playwright() as playwright:

  browser = playwright.chromium.launch(headless=False)
  context = browser.new_context()
  page = context.new_page()