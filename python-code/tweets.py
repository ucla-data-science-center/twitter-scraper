import asyncio
import signin
from playwright.async_api import async_playwright


async def my_async_function():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()

        # GOTO Twitter.com
        page = await context.new_page()
        await page.goto('https://twitter.com/home')
     
        await signin.sign_in(page, context)

        await context.close()

# Run the asynchronous function
asyncio.run(my_async_function())