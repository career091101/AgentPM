import asyncio
from playwright.async_api import async_playwright
import tempfile
import shutil

async def main():
    async with async_playwright() as p:
        tmp = tempfile.mkdtemp()
        print(f"Temp dir: {tmp}")
        try:
            print("Launching browser...")
            browser = await p.chromium.launch_persistent_context(
                tmp,
                headless=True,
                args=[
                    '--no-sandbox',
                    '--disable-setuid-sandbox',
                    '--disable-dev-shm-usage',
                    '--disable-blink-features=AutomationControlled'
                ],
                channel="chrome"
            )
            print("Launched successfully")
            page = browser.pages[0]
            await page.goto("https://example.com")
            print("Page loaded")
            await browser.close()
        except Exception as e:
            print(f"Failed: {e}")
        finally:
            try:
                shutil.rmtree(tmp)
            except:
                pass

if __name__ == "__main__":
    asyncio.run(main())
