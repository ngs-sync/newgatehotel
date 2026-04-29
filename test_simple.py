from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        file_path = "file://" + os.path.abspath("index.html")
        print(f"Loading {file_path}")
        page.goto(file_path)
        page.wait_for_timeout(2000)
        title = page.title()
        print(f"Title: {title}")
        root_html = page.inner_html("#root")
        print(f"Root HTML length: {len(root_html)}")
        if len(root_html) > 0:
            print("React rendered successfully")
        else:
            print("React failed to render")
        browser.close()

if __name__ == "__main__":
    run()
