from playwright.sync_api import sync_playwright
import parse;
import json
import time

file_name = "data.json"

def append_json_to_file(json_obj, file_name):
    """Append a JSON object to a file."""
    with open(file_name, 'a') as file:
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
        page.wait_for_selector("[data-testid='tweet']")

        # find all tweet background requests:
        tweet_calls = [f for f in _xhr_calls if "TweetResultByRestId" in f.url]
        for xhr in tweet_calls:
            data = xhr.json()
            return data['data']['tweetResult']['result']
        
if __name__ == "__main__":
    links = ['https://x.com/officialavatar/status/12054153920?s=20', 'https://x.com/officialavatar/status/10778452708?s=20', 'https://x.com/officialavatar/status/6805509694?s=20', 'https://x.com/officialavatar/status/6781426419?s=20', 'https://x.com/officialavatar/status/8486876370?s=20', 'https://x.com/officialavatar/status/8209994844?s=20', 'https://x.com/zoesaldana/status/8011663628?s=20', 'https://x.com/officialavatar/status/12185902884?s=20', 'https://x.com/officialavatar/status/6902888147?s=20', 'https://x.com/officialavatar/status/11763790953?s=20', 'https://x.com/officialavatar/status/12539954551?s=20', 'https://x.com/officialavatar/status/7955319799?s=20', 'https://x.com/officialavatar/status/11374498628?s=20', 'https://x.com/officialavatar/status/11261878822?s=20', 'https://x.com/officialavatar/status/7724615625?s=20', 'https://x.com/officialavatar/status/9203144344?s=20', 'https://x.com/officialavatar/status/11044239072?s=20', 'https://x.com/officialavatar/status/8257005681?s=20', 'https://x.com/officialavatar/status/12291033821?s=20', 'https://x.com/officialavatar/status/11830775822?s=20', 'https://x.com/officialavatar/status/10559022683?s=20', 'https://x.com/officialavatar/status/11007315736?s=20', 'https://x.com/officialavatar/status/12587029399?s=20', 'https://x.com/officialavatar/status/6955752053?s=20', 'https://x.com/officialavatar/status/7895808052?s=20', 'https://x.com/zoesaldana/status/8635491416?s=20', 'https://x.com/officialavatar/status/11004195935?s=20', 'https://x.com/officialavatar/status/12239591600?s=20', 'https://x.com/officialavatar/status/12135170584?s=20', 'https://x.com/officialavatar/status/11487915455?s=20', 'https://x.com/officialavatar/status/8001601495?s=20', 'https://x.com/officialavatar/status/9388777246?s=20', 'https://x.com/officialavatar/status/12355130572?s=20', 'https://x.com/officialavatar/status/10952461506?s=20', 'https://x.com/officialavatar/status/12230436761?s=20', 'https://x.com/officialavatar/status/8334278736?s=20', 'https://x.com/officialavatar/status/10625125370?s=20', 'https://x.com/leonalewis/status/8028480766?s=20', 'https://x.com/officialavatar/status/7470732528?s=20', 'https://x.com/officialavatar/status/10731544338?s=20', 'https://x.com/officialavatar/status/11648175183?s=20']
    for link in links:
        append_json_to_file(parse.dict_to_json(scrape_tweet(link)), file_name)