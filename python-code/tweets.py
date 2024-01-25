import asyncio
import signin
import time
from playwright.async_api import async_playwright
import tkinter as tk

async def my_async_function():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()

        # GOTO Twitter.com
        page = await context.new_page()
        await page.goto('https://twitter.com/home')
     
        await signin.sign_in(page, context)

        links = []

        for i in range(20):
            get_links = await page.query_selector_all('[aria-label="Share post"]')
            for get_link in get_links:
                await get_link.click()
                await page.get_by_text("Copy link").click()
                root = tk.Tk()
                # keep the window from showing
                root.withdraw()
                # read the clipboard
                c = root.clipboard_get()
                print(c)

            page.mouse.wheel(0, 500)
            time.sleep(3)

        input("Press Enter to close the browser...")

        await context.close()

# Run the asynchronous function
asyncio.run(my_async_function())