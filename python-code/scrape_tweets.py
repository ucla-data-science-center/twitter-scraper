from playwright.sync_api import sync_playwright
import parse;
import json
import time

file_name = "data.json"

def append_json_to_file(json_obj):
    """Append a JSON object to a file."""
    with open("unordered.json", 'a') as file:
        # Convert JSON object to string and write it to file
        # json_string = json.dumps(json_obj) + "\n"
        # print(json_string)
        file.write(json.dumps(json_obj) + "\n")



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
    links = ['https://x.com/MarkRuffalo/status/1123578131271516160?s=20', 'https://x.com/MarkRuffalo/status/1136719127807234048?s=20', 'https://x.com/Avengers/status/1153049064126259201?s=20', 'https://x.com/Avengers/status/1154783439092162560?s=20', 'https://x.com/MarkRuffalo/status/1129744083675734017?s=20', 'https://x.com/MarkRuffalo/status/1141095565771583488?s=20', 'https://x.com/MarkRuffalo/status/1120758180760440832?s=20', 'https://x.com/astromeda_game/status/1742229012146192783?s=20', 'https://x.com/Avengers/status/1153379186125332481?s=20', 'https://x.com/RobertDowneyJr/status/1144271720003452928?s=20', 'https://x.com/MarkRuffalo/status/1120517338028179461?s=20', 'https://x.com/MarkRuffalo/status/1102977073977540609?s=20', 'https://x.com/MarkRuffalo/status/1143588754914992128?s=20', 'https://x.com/sgonzaleezzz/status/1759952796651053495?s=20', 'https://x.com/MarkRuffalo/status/1118226985686376449?s=20', 'https://x.com/Avengers/status/1153045920033980417?s=20', 'https://x.com/Avengers/status/1153008459379556354?s=20', 'https://x.com/CambriaFunds/status/1489385930469249024?s=20', 'https://x.com/MarkRuffalo/status/1121881078552256514?s=20', 'https://x.com/DynastySands/status/1757173988361482317?s=20', 'https://x.com/MarkRuffalo/status/1113062174992166912?s=20', 'https://x.com/Avengers/status/1155145826571902976?s=20', 'https://x.com/MarkRuffalo/status/1092235693840048128?s=20', 'https://x.com/MarkRuffalo/status/1120809276094722051?s=20', 'https://x.com/Avengers/status/1153008271961284608?s=20', 'https://x.com/Avengers/status/1155870530395922434?s=20', 'https://x.com/MarkRuffalo/status/1150406223277117440?s=20', 'https://x.com/MarkRuffalo/status/1118867060640157696?s=20', 'https://x.com/MarkRuffalo/status/1076243917824090113?s=20', 'https://x.com/Avengers/status/1153010561703170049?s=20', 'https://x.com/Avengers/status/1153033413600972800?s=20', 'https://x.com/MarkRuffalo/status/1145681634907348993?s=20', 'https://x.com/Avengers/status/1153002974962159616?s=20', 'https://x.com/Avengers/status/1155915897132834819?s=20', 'https://x.com/Avengers/status/1154073761538355202?s=20', 'https://x.com/MarkRuffalo/status/1120774194361507844?s=20', 'https://x.com/MarkRuffalo/status/1114920769946050560?s=20', 'https://x.com/MarkRuffalo/status/1122854971148574723?s=20', 'https://x.com/MarkRuffalo/status/1115009747147735040?s=20', 'https://x.com/MarkRuffalo/status/1132648476389597186?s=20', 'https://x.com/MarkRuffalo/status/1108760181519929344?s=20', 'https://x.com/MarkRuffalo/status/1110572118448787457?s=20', 'https://x.com/Avengers/status/1153017289299628032?s=20', 'https://x.com/MarkRuffalo/status/1154458756853510144?s=20', 'https://x.com/kerzoven/status/1759896310587552019?s=20', 'https://x.com/MarkRuffalo/status/1120424536619589633?s=20', 'https://x.com/Avengers/status/1152997617200181249?s=20', 'https://x.com/MarkRuffalo/status/1125417742998364161?s=20', 'https://x.com/MarkRuffalo/status/1106194193037316096?s=20', 'https://x.com/SecurePhotosHQ/status/1683810087834468352?s=20', 'https://x.com/MarkRuffalo/status/1130126513330900994?s=20', 'https://x.com/Avengers/status/1153036622847459329?s=20', 'https://x.com/MarkRuffalo/status/1116007793419522049?s=20', 'https://x.com/Avengers/status/1153009508614115328?s=20', 'https://x.com/NeverMyFault_/status/1754490053806686562?s=20', 'https://x.com/RobertDowneyJr/status/1110572366772330496?s=20', 'https://x.com/Avengers/status/1155191123494801408?s=20', 'https://x.com/MarkRuffalo/status/1114698519045136384?s=20', 'https://x.com/Avengers/status/1152995870167752706?s=20', 'https://x.com/MarkRuffalo/status/1140979445693669378?s=20', 'https://x.com/MarkRuffalo/status/1112706931565703169?s=20', 'https://x.com/Avengers/status/1155523312468078592?s=20', 'https://x.com/Avengers/status/1153711374184439808?s=20', 'https://x.com/MarkRuffalo/status/1122521511561183235?s=20', 'https://x.com/Avengers/status/1153002605464961024?s=20', 'https://x.com/MarkRuffalo/status/1127982193450602499?s=20', 'https://x.com/MarkRuffalo/status/1125772878308421632?s=20', 'https://x.com/MarkRuffalo/status/1130482533299380225?s=20']
    for link in links:
        append_json_to_file(parse.dict_to_json(scrape_tweet(link)))