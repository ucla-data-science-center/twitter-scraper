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
        
        time.sleep(0.5)
        retry = page.get_by_text("Retry")

        if (retry.is_visible()):
            # print("found")
            retry.click()
            time.sleep(1)
            # page.wait_for_selector("[data-testid='tweet']")
        # else:
            # print("here")
            # page.wait_for_selector("[data-testid='tweet']")
        dne = page.get_by_text("Hmm...this page doesn’t exist. Try searching for something else.")
        if (dne.is_visible()):
            page.close()
            return

        time.sleep(1)
        page.wait_for_selector("[data-testid='tweet']")
        

        # find all tweet background requests:
        tweet_calls = [f for f in _xhr_calls if "TweetResultByRestId" in f.url]
        for xhr in tweet_calls:
            data = xhr.json()
            return data['data']['tweetResult']['result']
        
if __name__ == "__main__":
    links = ['https://x.com/KarimaSulleyman/status/1625243624702111747?s=20', 'https://x.com/Tom_Muzzy_2001/status/1624920634491916288?s=20', 'https://x.com/Khang1Tn/status/1641247775097786368?s=20', 'https://x.com/Titansszn9/status/1624916076764209152?s=20', 'https://x.com/BattinsonMarvel/status/1624916481405247489?s=20', 'https://x.com/YAM_LADYBUG/status/1625002001439522817?s=20', 'https://x.com/SubhanKhan_157/status/1642903305356554240?s=20', 'https://x.com/JoshUltra/status/1625139072946814977?s=20', 'https://x.com/ehite_haque/status/1624923989423390722?s=20', 'https://x.com/archangelzxv/status/1624916911359397888?s=20', 'https://x.com/ResSnyderVerse/status/1624938023929491457?s=20', 'https://x.com/ResSnyderVerse/status/1624938002806894593?s=20', 'https://x.com/AlexisMCh1996/status/1624935296050638851?s=20', 'https://x.com/Guardians/status/1624915963970981889?s=20', 'https://x.com/HPBarb1965/status/1624919300036231168?s=20', 'https://x.com/IMAX/status/1624917606233948162?s=20', 'https://x.com/jaychau29837328/status/1625153404761931781?s=20', 'https://x.com/morboywnder/status/1624939151022776320?s=20', 'https://x.com/MrShovel_048/status/1624934590660894721?s=20', 'https://x.com/DuckMastan/status/1625082663903330304?s=20', 'https://x.com/nybigtymer/status/1624916912651272194?s=20', 'https://x.com/DIMENSION_YT/status/1624922203236990976?s=20', 'https://x.com/jcnaturalgas/status/1639620460248743938?s=20', 'https://x.com/Mr_Loco_83/status/1624916861757591553?s=20', 'https://x.com/trinsesEls/status/1624930593627860993?s=20', 'https://x.com/GhostByteRyan/status/1624919669697302528?s=20', 'https://x.com/JustinAzevedo10/status/1624918724326330368?s=20', 'https://x.com/adjei_blebo/status/1625080728202498048?s=20', 'https://x.com/LenaAxios/status/1624918768202706944?s=20', 'https://x.com/GuilleHD/status/1624916410425024514?s=20', 'https://x.com/SoulCellular/status/1624983969220505602?s=20', 'https://x.com/Sergomatic/status/1624953950993784834?s=20', 'https://x.com/ColbySteffens/status/1624944468473389056?s=20', 'https://x.com/Enric_orts/status/1625021176434008064?s=20', 'https://x.com/MasinAlfredo/status/1625191399380422665?s=20', 'https://x.com/RomaeroNova/status/1624923736850763776?s=20', 'https://x.com/ScorpVayne/status/1632494779186438155?s=20', 'https://x.com/alriefandidi/status/1625020653576527872?s=20', 'https://x.com/Secoh2000/status/1625124786979618816?s=20', 'https://x.com/UKMarvelLegends/status/1625068575688994816?s=20', 'https://x.com/abbe_farria/status/1624923686884020224?s=20', 'https://x.com/brattyishappy/status/1624966379500720129?s=20', 'https://x.com/JPaulo645/status/1624918136431443968?s=20', 'https://x.com/Mrshelby_21/status/1624921323892838402?s=20', 'https://x.com/IronMitchXL/status/1625018753548431363?s=20', 'https://x.com/xavier_rayana/status/1624944346809176064?s=20', 'https://x.com/InGandalf/status/1624946817400991745?s=20', 'https://x.com/Qhue_the_mad/status/1624916898730082307?s=20', 'https://x.com/RyanReaXts/status/1624920747218010112?s=20', 'https://x.com/linu2/status/1625099766190206976?s=20', 'https://x.com/edwardistheman/status/1624916299376742400?s=20', 'https://x.com/hacksocial_ai/status/1627526320887582721?s=20', 'https://x.com/MynameGuff/status/1624916764927614978?s=20', 'https://x.com/SDagger02/status/1624946782949060616?s=20', 'https://x.com/Honey_Heidi360/status/1641937534174330882?s=20', 'https://x.com/Alex4kUltra/status/1624934097884676097?s=20', 'https://x.com/JamesGunn/status/1624918626125119488?s=20', 'https://x.com/mvg512/status/1624920744814600192?s=20', 'https://x.com/redManc213/status/1625014659211198466?s=20', 'https://x.com/RyanReaXts/status/1624918849882554372?s=20', 'https://x.com/hopevndyneswife/status/1624918415210082308?s=20', 'https://x.com/yamora_permata/status/1624921933807775745?s=20', 'https://x.com/DavidLezette/status/1624917294634631169?s=20', 'https://x.com/TheCinefanatics/status/1624938273146605577?s=20', 'https://x.com/BarbaraMcDevitt/status/1624923874092630016?s=20', 'https://x.com/ShaneDedon/status/1624916186398859264?s=20', 'https://x.com/Ayyub4Ayyub/status/1625175655523704840?s=20', 'https://x.com/BrianaHonack7/status/1644036016314146817?s=20', 'https://x.com/hehekarlahaha/status/1625035004265865218?s=20', 'https://x.com/sairapphael/status/1624945545243668481?s=20', 'https://x.com/nicolejasmin_pw/status/1625319217431019521?s=20', 'https://x.com/KangAnfield8/status/1624940707617329152?s=20', 'https://x.com/ju8nnnn/status/1624941692871745536?s=20', 'https://x.com/Joefanatic23/status/1624916948906647554?s=20', 'https://x.com/nick2amazing/status/1625031875164008448?s=20', 'https://x.com/Khang1Tn/status/1641247783029211136?s=20', 'https://x.com/INSaneNShades/status/1624918844119650304?s=20', 'https://x.com/2011apowell/status/1624925067724324866?s=20', 'https://x.com/CyndiB123/status/1624928466801168384?s=20', 'https://x.com/daikou/status/1624918569040416768?s=20', 'https://x.com/Vairons_Split/status/1625036289836818433?s=20', 'https://x.com/justnoiresync/status/1624922370610978816?s=20', 'https://x.com/SPGear1/status/1624987920712056832?s=20', 'https://x.com/acalipp/status/1624929517893726208?s=20', 'https://x.com/ericisnotyoung/status/1626531009863843840?s=20', 'https://x.com/Jonathan46784/status/1624930077203996673?s=20', 'https://x.com/iu_lian92/status/1625056690482692096?s=20', 'https://x.com/RachelW94/status/1624916855289745408?s=20', 'https://x.com/Carson_Hudkins/status/1624916064395051010?s=20', 'https://x.com/ASm1thee/status/1624968400375095297?s=20', 'https://x.com/Rodrace/status/1624917745107075073?s=20', 'https://x.com/hulu/status/1624952543226007553?s=20', 'https://x.com/suertedu/status/1625012296937340928?s=20', 'https://x.com/Helena2340/status/1632009855438401537?s=20', 'https://x.com/ConnorBTweets/status/1628119577623203843?s=20', 'https://x.com/Terror__Con/status/1624921059811106816?s=20', 'https://x.com/MILTONCRISTVAO/status/1625009566520954882?s=20', 'https://x.com/JohnProyect/status/1625029447421231107?s=20']
    for link in links:
        append_json_to_file(parse.dict_to_json(scrape_tweet(link)))