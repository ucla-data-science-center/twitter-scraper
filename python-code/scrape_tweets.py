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
        
        time.sleep(1)
        retry = page.get_by_text("Retry")

        if (retry.is_visible()):
            # print("found")
            retry.click()
            time.sleep(1)
            # page.wait_for_selector("[data-testid='tweet']")
        # else:
            # print("here")
            # page.wait_for_selector("[data-testid='tweet']")
        time.sleep(1)
        page.wait_for_selector("[data-testid='tweet']")
        

        # find all tweet background requests:
        tweet_calls = [f for f in _xhr_calls if "TweetResultByRestId" in f.url]
        for xhr in tweet_calls:
            data = xhr.json()
            return data['data']['tweetResult']['result']
        
if __name__ == "__main__":
    links = ['https://x.com/DaveBautista/status/439116959402041344?s=20', 'https://x.com/prattprattpratt/status/510470937368875009?s=20', 'https://x.com/Guardians/status/495599961006800896?s=20', 'https://x.com/prattprattpratt/status/474668157383487488?s=20', 'https://x.com/Guardians/status/456182695035285504?s=20', 'https://x.com/prattprattpratt/status/440653731298697216?s=20', 'https://x.com/zoesaldana/status/487376090063581184?s=20', 'https://x.com/Guardians/status/483705809172312064?s=20', 'https://x.com/zoesaldana/status/524349579383566336?s=20', 'https://x.com/prattprattpratt/status/534491171796840449?s=20', 'https://x.com/Guardians/status/487314853732691968?s=20', 'https://x.com/zoesaldana/status/468990571089235969?s=20', 'https://x.com/zoesaldana/status/487856669494214657?s=20', 'https://x.com/prattprattpratt/status/389030410992484352?s=20', 'https://x.com/zoesaldana/status/487377869849370624?s=20', 'https://x.com/prattprattpratt/status/476183040352202752?s=20', 'https://x.com/prattprattpratt/status/492712765262278658?s=20', 'https://x.com/prattprattpratt/status/436328694135525376?s=20', 'https://x.com/Guardians/status/499255712212463616?s=20', 'https://x.com/Guardians/status/491678570486312961?s=20', 'https://x.com/DaveBautista/status/487773943349006336?s=20', 'https://x.com/prattprattpratt/status/447099071614828544?s=20', 'https://x.com/Guardians/status/373557265631961088?s=20', 'https://x.com/prattprattpratt/status/353573354608922624?s=20', 'https://x.com/zoesaldana/status/363064213368877056?s=20', 'https://x.com/Guardians/status/501792779513888768?s=20', 'https://x.com/prattprattpratt/status/436601985316298752?s=20', 'https://x.com/DaveBautista/status/494690915881996288?s=20', 'https://x.com/Guardians/status/468074347215609856?s=20', 'https://x.com/prattprattpratt/status/435823934030630912?s=20', 'https://x.com/DaveBautista/status/341560449608867840?s=20']
    for link in links:
        append_json_to_file(parse.dict_to_json(scrape_tweet(link)))