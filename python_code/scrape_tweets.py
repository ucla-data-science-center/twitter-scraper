from playwright.sync_api import sync_playwright
import parse;
import json
import time

file_name = "data.json"

def append_json_to_file(json_obj):
    """Append a JSON object to a file."""
    with open("./data/unordered.json", 'a') as file:
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
        
        page.wait_for_timeout(500)
        retry = page.get_by_text("Retry")

        if (retry.is_visible()):
            retry.click()
            page.wait_for_timeout(1000)

        dne = page.get_by_text("Hmm...this page doesn’t exist. Try searching for something else.")
        if (dne.is_visible()):
            page.close()
            return
        try_again = page.get_by_text("Try Again")
        if (try_again.is_visible()):
            try_again.click()
            page.wait_for_timeout(1000)
        
        page.wait_for_timeout(500)
        page.wait_for_selector("[data-testid='tweet']")

        # find all tweet background requests:
        tweet_calls = [f for f in _xhr_calls if "TweetResultByRestId" in f.url]
        for xhr in tweet_calls:
            data = xhr.json()
            return data['data']['tweetResult']['result']
        
if __name__ == "__main__":
    links = ['https://x.com/zukomaximoff/status/1493004037272309760?s=20', 'https://x.com/theusmatag/status/1493005131327156228?s=20', 'https://x.com/fluffykittensox/status/1493001299805229058?s=20', 'https://x.com/RJFlamingo/status/1493007917355880449?s=20', 'https://x.com/azizul_za/status/1493000985710833667?s=20', 'https://x.com/yoongisoo1/status/1493000933466378245?s=20', 'https://x.com/IWolfSong/status/1493003735185903628?s=20', 'https://x.com/mythos1014/status/1493001035995959298?s=20', 'https://x.com/hopexrih/status/1493000455387025409?s=20', 'https://x.com/ChelseaDMorning/status/1493002329796272128?s=20', 'https://x.com/toniapelagica/status/1493001819470983174?s=20', 'https://x.com/fznfznfznfzn/status/1493004500738662400?s=20', 'https://x.com/yeeuncrop/status/1493004071426424834?s=20', 'https://x.com/24KTV96/status/1493001408009977859?s=20', 'https://x.com/alx_uz/status/1493002519664107531?s=20', 'https://x.com/I_StayFitted/status/1493005717749518336?s=20', 'https://x.com/KennethKolton/status/1493013849540206593?s=20', 'https://x.com/QuaIil/status/1493005813484511232?s=20', 'https://x.com/ColinCampbellyt/status/1493001779830833153?s=20', 'https://x.com/Miss_Eva263/status/1493252189124448256?s=20', 'https://x.com/llysistrataa/status/1493003562149978115?s=20', 'https://x.com/Hyo_Joestar/status/1493005659440357380?s=20', 'https://x.com/cardigaans/status/1493007646764711936?s=20', 'https://x.com/ThoughtPillow/status/1493149740678238208?s=20', 'https://x.com/YoloBlaziken/status/1493001336539033604?s=20', 'https://x.com/kxrinarosas/status/1493001338342543364?s=20', 'https://x.com/coquitooFN/status/1493003497645785095?s=20', 'https://x.com/halebskisses/status/1493000502795251713?s=20', 'https://x.com/arafat_thfc/status/1493004662974332928?s=20', 'https://x.com/brainrotbot1/status/1493001949733695490?s=20', 'https://x.com/iivanandress/status/1493003180275388422?s=20', 'https://x.com/elvisxxs/status/1493000460516605959?s=20', 'https://x.com/cheiratiner/status/1493005552330420228?s=20', 'https://x.com/hcgeanine/status/1493009109641277450?s=20', 'https://x.com/goohopes/status/1493002200775278594?s=20', 'https://x.com/n70reecee/status/1493012142173347844?s=20', 'https://x.com/Kibet98/status/1493000851404644352?s=20', 'https://x.com/DJizLurch/status/1493009166121803776?s=20', 'https://x.com/oliviamcc19/status/1493006263403397120?s=20', 'https://x.com/jayxmercury14/status/1493001175716831234?s=20', 'https://x.com/fuioseuprimeiro/status/1493008455233384448?s=20', 'https://x.com/cevnsortega/status/1493006798336442379?s=20', 'https://x.com/alecbustos/status/1493005464325574661?s=20', 'https://x.com/ReferraI/status/1493000757863456768?s=20', 'https://x.com/loveandjusticee/status/1493002271755431940?s=20', 'https://x.com/JBarroilhet/status/1493005788654313472?s=20', 'https://x.com/bookish_bees/status/1493001538624794627?s=20', 'https://x.com/revefolklore/status/1493002669723725825?s=20', 'https://x.com/btstayariana1/status/1493002126154420226?s=20', 'https://x.com/akwong31/status/1493004151369912321?s=20', 'https://x.com/estevomon/status/1493004688375128064?s=20', 'https://x.com/nadaelmikashfi/status/1493000608525295622?s=20', 'https://x.com/GuyroWasTaken/status/1493000680172314626?s=20', 'https://x.com/Theodev420/status/1493005162465710082?s=20', 'https://x.com/byel233/status/1493000708764938240?s=20', 'https://x.com/cxlixcali/status/1493000645149962241?s=20', 'https://x.com/Martinc4v8/status/1493003050264395778?s=20', 'https://x.com/Scykology/status/1493002502001811457?s=20', 'https://x.com/6e3rr/status/1493000740519952384?s=20', 'https://x.com/Darkfireunicorn/status/1493001730736414721?s=20', 'https://x.com/t2trilll/status/1493176432901689344?s=20', 'https://x.com/sofydumpp/status/1493001307619266570?s=20', 'https://x.com/AyeYoRavy/status/1493004191840800769?s=20', 'https://x.com/NotIsaiah__/status/1493001413202427908?s=20', 'https://x.com/boochieboots/status/1493004050140385286?s=20', 'https://x.com/EdwardIsSoCool/status/1493000555811192841?s=20', 'https://x.com/migueldboada1/status/1493000670198341640?s=20', 'https://x.com/Brian_Lightyear/status/1493004396795412480?s=20', 'https://x.com/yoongisoo1/status/1493000908405452804?s=20', 'https://x.com/wandasplaylist/status/1493004222706720773?s=20', 'https://x.com/ronsalas/status/1493000619313012736?s=20', 'https://x.com/eivamax/status/1493000787139641344?s=20', 'https://x.com/brianjordant/status/1493006347754893314?s=20', 'https://x.com/TswiftStreet/status/1493002681941733381?s=20', 'https://x.com/spencer13__/status/1493001194431787010?s=20', 'https://x.com/UrbanNoize2/status/1493012019657728002?s=20', 'https://x.com/EARTH_1610_616/status/1493002582838681603?s=20', 'https://x.com/BrandonMusicKy/status/1493012288823078917?s=20', 'https://x.com/fadzrulafzal/status/1493003205021937671?s=20', 'https://x.com/DeyvidAguiar3/status/1493008782821048320?s=20', 'https://x.com/JayFlaco_/status/1493001142069981187?s=20', 'https://x.com/Ramonzhada/status/1493002920543100930?s=20', 'https://x.com/Kevin_Happy_xx/status/1493000486500323334?s=20', 'https://x.com/JonLReyes/status/1493005984180019202?s=20', 'https://x.com/CG172_/status/1493000804600528900?s=20']
    for link in links:
        results = parse.dict_to_json(scrape_tweet(link))
        if results != None:
            append_json_to_file(results)