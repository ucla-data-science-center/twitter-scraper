from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright
import json
import asyncio
import time
import signin
import tkinter as tk

async def scrape_links(url: str, sign_in: bool, context):
    async with async_playwright() as p:
        links = set()
        page = await context.new_page()
        await page.goto(url)

        if sign_in:
            await signin.sign_in(page, context)
            time.sleep(2)

        await page.goto(url)
        
        i = 0
        try:
            # Collects 200 links
            while i < 200 and len(links) < 200:
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

async def scrape_comments():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        for tweet in m_tweets:
            links = await scrape_links(tweet, tweet == m_tweets[0], context)
            with open("links.txt", 'a') as file:
                file.write(str(links))
                file.write("\n")

        await context.close()

if __name__ == "__main__":
    m_tweets = ["https://x.com/supermariomovie/status/1597714544641687553?s=46"]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(scrape_comments())
    loop.close()

