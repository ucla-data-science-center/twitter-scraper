import asyncio
from playwright.async_api import async_playwright
import os
from dotenv import load_dotenv

load_dotenv()

async def sign_in(page, context):
    async with async_playwright() as p:
        google_sign_in = await page.wait_for_selector("[data-testid='google_sign_in_container']")

        async with context.expect_page() as new_page_info:
            await google_sign_in.hover()
            await google_sign_in.click()
        
        # Handle Popup
        new_page = await new_page_info.value
        await new_page.wait_for_load_state()

        # Enter your email
        enter_email = await new_page.wait_for_selector("[type='email']")
        await enter_email.click()
        await enter_email.type(os.getenv("UCLA_EMAIL"))

        # Click Next
        await new_page.get_by_text("Next").click()
        
        # Input UCLA Username
        input_field = await new_page.wait_for_selector("[placeholder='Your UCLA Logon ID']")
        await input_field.click()
        await input_field.type(os.getenv("UCLA_LOGON"))
        # Input UCLA Password
        input_field = await new_page.wait_for_selector("[placeholder='Your UCLA Logon Password']")
        await input_field.click()
        await input_field.type(os.getenv("UCLA_PASSWORD"))

        # Click on Sign In
        sign_in = await new_page.wait_for_selector(("[type='submit']"))
        await sign_in.click()

        # Click on "Yes, this is my device" After Duopush
        await new_page.get_by_text("Yes, this is my device").click()

        # Choose Account
        final_click = await new_page.wait_for_selector('[aria-labelledby="picker-item-label-0"]')
        await final_click.click()