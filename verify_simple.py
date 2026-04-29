from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        file_path = "file://" + os.path.abspath("index.html")
        page.goto(file_path)
        page.wait_for_timeout(2000)
        page.screenshot(path="simple_screenshot.png")
        print("Screenshot taken: simple_screenshot.png")
        browser.close()

if __name__ == "__main__":
    run()
