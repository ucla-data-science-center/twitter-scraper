# import asyncio
import signin
import time
from playwright.async_api import async_playwright
import tkinter as tk

async def my_async_function(url: str, sign_in: bool, context):
    async with async_playwright() as p:
        # browser = await p.chromium.launch(headless=False)
        # context = await browser.new_context()
        links = set()
        # GOTO Twitter.com
        page = await context.new_page()
        await page.goto(url)

        if sign_in:
            await signin.sign_in(page, context)
            time.sleep(2)

        await page.goto(url)

        try:
            # await page.get_by_text("Retry").click()
            
            for i in range(20):
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

                await page.mouse.wheel(0, 500)
                time.sleep(2)
        except:
            await page.close()
            return links
 
        # await context.close()
        await page.close()
        return links

# Run the asynchronous function
# asyncio.run(my_async_function())

# https://x.com/EverythingOOC/status/1749896346646057227?s=20
# https://x.com/ayeejuju/status/1750207385036317007?s=20
# https://x.com/TweetsOfCats/status/1749948636924903934?s=20
# https://x.com/s8n/status/1749990468165730731?s=20
# https://x.com/EverythingOOC/status/1749896346646057227?s=20
# https://x.com/ayeejuju/status/1750207385036317007?s=20
# https://x.com/TweetsOfCats/status/1749948636924903934?s=20
# https://x.com/s8n/status/1749990468165730731?s=20
# https://x.com/historyinmemes/status/1750180154700382698?s=20
# https://x.com/Yoda4ever/status/1750154075193450714?s=20
# https://x.com/TheFigen_/status/1749787040722334073?s=20
# https://x.com/interesting_aIl/status/1749658733032898962?s=20
# https://x.com/Yoda4ever/status/1750154075193450714?s=20
# https://x.com/TheFigen_/status/1749787040722334073?s=20
# https://x.com/interesting_aIl/status/1749658733032898962?s=20
# https://x.com/PicturesFoIder/status/1749751077061492911?s=20
# https://x.com/Whotfismick/status/1750015580277539132?s=20