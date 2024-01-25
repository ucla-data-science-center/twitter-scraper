import asyncio
import signin
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

        # for li in await page.get_by_role('listitem').all():
        #     await li.click();

        sup = await page.get_by_label("Share post").all()

        # aria-label="Share post"

        print(len(sup))

        get_link = await page.wait_for_selector('[aria-label="Share post"]')
        await get_link.click()

        await page.get_by_text("Copy link").click()

        # print(get_link)

        root = tk.Tk()
        # keep the window from showing
        root.withdraw()

        # read the clipboard
        c = root.clipboard_get()

        # print(c)

        input("Press Enter to close the browser...")

        await context.close()

# Run the asynchronous function
asyncio.run(my_async_function())