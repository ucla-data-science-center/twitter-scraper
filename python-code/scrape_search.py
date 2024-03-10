# import asyncio
import signin
import time
from playwright.async_api import async_playwright
import tkinter as tk

async def scrape_search(url: str, sign_in: bool, context):
    async with async_playwright() as p:
        links = set()
        page = await context.new_page()
        await page.goto(url)

        if sign_in:
            await signin.sign_in(page, context)
            time.sleep(2)

        await page.goto(url)
        
        
        try:
            for i in range(50):
                if (await page.get_by_text("Retry").is_visible()):
                    await page.get_by_text("Retry").click()
                get_links = await page.query_selector_all('[aria-label="Share post"]')
                for get_link in get_links:
                    if (await get_link.is_visible()):
                        await get_link.hover()
                        await get_link.click()
                        await page.get_by_text("Copy link").click()
                        root = tk.Tk()
                        # keep the window from showing
                        root.withdraw()
                        # read the clipboard
                        c = root.clipboard_get()
                        links.add(c)
                    else:
                        if await page.get_by_text("Retry").is_visible():
                            await page.get_by_text("Retry").click()
                await page.mouse.wheel(0, 1000)
                time.sleep(2)
        except:
            await page.close()
            return links
 
        # await context.close()
        await page.close()
        return links