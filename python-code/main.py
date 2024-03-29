# PACKAGES
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright
import json
import asyncio

# HELPER FUNCTIONS
import query
import scrape_search
import parse

def scrape_tweet(url: str) -> dict:
    """
    Scrape a single tweet page for Tweet thread e.g.:
    https://twitter.com/Scrapfly_dev/status/1667013143904567296
    Return parent tweet, reply tweets and recommended tweets
    """
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
        page.goto(url)
        page.wait_for_selector("[data-testid='tweet']")

        # find all tweet background requests:
        tweet_calls = [f for f in _xhr_calls if "TweetResultByRestId" in f.url]
        for xhr in tweet_calls:
            data = xhr.json()
            return data['data']['tweetResult']['result']


def read_json(path: str) -> list:
    res = []
    f = open(path)
    data = json.load(f)
    
    # Iterating through the json
    # list
    for i in data:
        res.append(i)
    # Closing file
    f.close()
    return res

async def scrape_links():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        for search in searches:
            keyword = search["Keywords"]
            accounts = [i.replace("@", "") for i in search["Accounts"].split(", ")]
            start_date = parse.convert_to_date(search.get("Start Date", None))
            end_date = parse.convert_to_date(search.get("End Date", None))
            exact_phrase = search.get("Exact Phrase", None)
            any_phrase = search.get("Any Phrase", None)
            hashtags = search.get("Hashtags", None)
            search_query = query.query_builder(keyword=keyword, from_account=accounts, start_date=start_date, end_date=end_date, 
                                               exact_phrase=exact_phrase, any_phrase=any_phrase, hashtags=hashtags)
            links = await scrape_search.scrape_search(search_query, search == searches[0], context)
            with open("links.txt", 'a') as file:
                file.write(str(links))
                file.write("\n")

        await context.close()



if __name__ == "__main__":
    searches = read_json("data/search.json")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(scrape_links())
    loop.close()
