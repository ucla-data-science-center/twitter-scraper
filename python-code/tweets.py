from playwright.sync_api import sync_playwright

def retrieve_tweets() -> list:
    res = []

    _xhr_calls = []

    def intercept_response(response):
        """capture all background requests and save them"""
        # we can extract details from background requests
        if response.request.resource_type == "xhr":
            _xhr_calls.append(response)
        return response

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        # enable background request intercepting:
        page.on("response", intercept_response)
        # go to url and wait for the page to load
        
        page.goto("https://twitter.com/home")
        href_element = page.wait_for_selector("a")
        print(href_element)
        page.wait_for_selector("[data-testid='tweet']")

    return res

retrieve_tweets()