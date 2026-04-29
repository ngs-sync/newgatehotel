from playwright.sync_api import sync_playwright
import os
import sys

def run():
    try:
        with sync_playwright() as p:
            print("Launching browser...")
            browser = p.chromium.launch()
            page = browser.new_page()
            file_path = "file://" + os.path.abspath("index.html")
            print(f"Navigating to {file_path}")
            page.goto(file_path)
            print("Waiting for load...")
            page.wait_for_timeout(3000)

            # Print page content length
            content = page.content()
            print(f"Content length: {len(content)}")

            # Print console messages
            page.on("console", lambda msg: print(f"BROWSER CONSOLE: {msg.text}"))
            page.on("pageerror", lambda err: print(f"BROWSER ERROR: {err.message}"))

            # Inject session
            print("Injecting session...")
            page.evaluate('''() => {
                localStorage.setItem('hotel_session', JSON.stringify({
                    tenant_id: 'GATES-001',
                    full_name: 'Test Admin',
                    role: 'hotel_admin',
                    email: 'admin@test.com'
                }));
            }''')
            page.reload()
            page.wait_for_timeout(3000)

            print(f"Title: {page.title()}")

            # Take screenshot
            screenshot_path = "final_verify.png"
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")

            # Check for React root
            root_exists = page.query_selector("#root > div") is not None
            print(f"React rendered div inside root: {root_exists}")

            browser.close()
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    run()
