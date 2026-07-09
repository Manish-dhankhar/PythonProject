from playwright.sync_api import Playwright, sync_playwright
import pytest

def test_APIrequestcontext(playwright):
 request = playwright.request.new_context()
 response = request.get("https://practice.expandtesting.com/notes/api/health-check")
 print(response.status)
 assert response.status == 200
 json_result= response.json()
 print(json_result)
 #print(result)
 request.dispose()