from playwright.sync_api import sync_playwright
import parse;
import json
import time

file_name = "data.json"

def append_json_to_file(json_obj):
    """Append a JSON object to a file."""
    with open("unordered.json", 'a') as file:
        # Convert JSON object to string and write it to file
        json_string = json.dumps(json_obj) + "\n"
        file.write(json_string)



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
        
        retry = page.get_by_text("Retry")

        if (retry.is_visible()):
            print("found")
            retry.click()
            time.sleep(0.5)
        else:
            print("here")

        page.wait_for_selector("[data-testid='tweet']")
        

        # find all tweet background requests:
        tweet_calls = [f for f in _xhr_calls if "TweetResultByRestId" in f.url]
        for xhr in tweet_calls:
            data = xhr.json()
            return data['data']['tweetResult']['result']
        
if __name__ == "__main__":
    links = []
    for link in links:
        append_json_to_file(parse.dict_to_json(scrape_tweet(link)))