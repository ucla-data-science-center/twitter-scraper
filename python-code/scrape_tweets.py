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
    links = ['https://x.com/DomainD_/status/1597714680734445568?s=20', 'https://x.com/MattDaRedPilled/status/1597747689248411648?s=20', 'https://x.com/AxolotlSimp/status/1597716996455825409?s=20', 'https://x.com/pono_onop/status/1598701901419147264?s=20', 'https://x.com/_kevosan/status/1597725784411885573?s=20', 'https://x.com/DillonGeor/status/1597715963381940225?s=20', 'https://x.com/ScottySacam97/status/1597747393331884032?s=20', 'https://x.com/pongondonute/status/1597729531447889920?s=20', 'https://x.com/Venom_man4/status/1597721795276451841?s=20', 'https://x.com/TheRealCoolmath/status/1597741714441007104?s=20', 'https://x.com/whtareyoubying/status/1597727875968663552?s=20', 'https://x.com/DatSimpleNope/status/1597830527486398465?s=20', 'https://x.com/Brad_801/status/1637850125564526593?s=20', 'https://x.com/GJ_Doggy/status/1597722094196129792?s=20', 'https://x.com/pencilforge/status/1597733850871828480?s=20', 'https://x.com/BikeMan/status/1597799422406307840?s=20', 'https://x.com/Wykin6/status/1597715133773807617?s=20', 'https://x.com/4takuri_24/status/1597717367198740481?s=20', 'https://x.com/Marshmelodii/status/1597747004175572992?s=20', 'https://x.com/PabloPlanovsky/status/1597720194243182597?s=20', 'https://x.com/Theultimatesim9/status/1597716344434462720?s=20', 'https://x.com/anonymousgamef2/status/1597716281775788032?s=20', 'https://x.com/Benie76/status/1597752145402793984?s=20', 'https://x.com/Ken_on_Da_Moon/status/1598637286941507584?s=20', 'https://x.com/supermariomovie/status/1597714544641687553?s=20', 'https://x.com/theluma/status/1597736877431599104?s=20', 'https://x.com/Sage999XXX/status/1597715195014455296?s=20', 'https://x.com/devendaman/status/1597716036643880960?s=20', 'https://x.com/FlowtacKendall/status/1597746126555602949?s=20', 'https://x.com/Wolvenone/status/1597786160306491392?s=20', 'https://x.com/dominikmuggli/status/1624925469819953154?s=20', 'https://x.com/Mr_Zilla1/status/1597720043953192961?s=20', 'https://x.com/KellanRios/status/1597725704900472833?s=20', 'https://x.com/astrolotte/status/1597792185231216641?s=20', 'https://x.com/Ryan20615/status/1597714611419385857?s=20', 'https://x.com/Cam_Guy11/status/1597715315756249089?s=20', 'https://x.com/RobinPoedev/status/1597723649200750592?s=20', 'https://x.com/6M0TI/status/1597714628460806145?s=20', 'https://x.com/wydcrunchy/status/1597743142803222528?s=20', 'https://x.com/BiggieMane1/status/1597743529161551873?s=20', 'https://x.com/Stifle_Tower27/status/1597717691842072576?s=20', 'https://x.com/RevelXyz/status/1648685177495773187?s=20', 'https://x.com/LightTophat/status/1597716964067414017?s=20', 'https://x.com/Gon4KT_/status/1597714640846614530?s=20', 'https://x.com/gonsoos_banana/status/1597715012227063808?s=20', 'https://x.com/Brandon_Wolffe/status/1599948290048503810?s=20', 'https://x.com/JinathHyder/status/1597722019524915200?s=20', 'https://x.com/VirtualFireball/status/1597740185600786432?s=20', 'https://x.com/CryptoEmpressX/status/1622452030290952194?s=20', 'https://x.com/linkifie/status/1597715020212674560?s=20', 'https://x.com/LordeVitucci/status/1598140553077542912?s=20', 'https://x.com/_purpletay_/status/1597715308613373952?s=20', 'https://x.com/ChokingCrab/status/1597715829126467585?s=20', 'https://x.com/BikeMan/status/1597816068130889728?s=20', 'https://x.com/LupeSilverwind/status/1597719588359196672?s=20', 'https://x.com/RoboKy10/status/1597719676209201153?s=20', 'https://x.com/mcsquiddies/status/1597716162250674176?s=20', 'https://x.com/Twitch/status/1597735899118600192?s=20', 'https://x.com/S_O_J_K_A/status/1597799816779550720?s=20', 'https://x.com/luis_gj/status/1597723310376165376?s=20', 'https://x.com/SuperiorGothBun/status/1597715316066295808?s=20', 'https://x.com/VirtualKid64/status/1597717866425749505?s=20', 'https://x.com/Christalball93/status/1641993319986397185?s=20', 'https://x.com/DESESPER0/status/1598035658433761280?s=20', 'https://x.com/nononodag22/status/1597715170616569856?s=20', 'https://x.com/Sonic_E_F/status/1597715851435593728?s=20', 'https://x.com/ItsEdjailMendes/status/1631388628256473088?s=20', 'https://x.com/SperitB/status/1597826659637657600?s=20', 'https://x.com/NZXT/status/1597715684674637825?s=20', 'https://x.com/clarkejoseph49/status/1606007926392557575?s=20', 'https://x.com/riquelombardi/status/1597733263036280833?s=20', 'https://x.com/HaHaAiden/status/1597718028049088513?s=20', 'https://x.com/RainingJazz/status/1597716410947731456?s=20', 'https://x.com/Freebraveminds/status/1597817388950753281?s=20', 'https://x.com/mrcroissantguy/status/1597732811607531520?s=20', 'https://x.com/Taiconan1/status/1597812798897426432?s=20', 'https://x.com/KirbyEarthbound/status/1597714872694763520?s=20', 'https://x.com/TVMBLEZ/status/1597725592857632768?s=20', 'https://x.com/Melissa808HI/status/1597817564155215872?s=20', 'https://x.com/xxxxVASHxxxx/status/1597789756921761793?s=20', 'https://x.com/PrideRing666/status/1597719196213071872?s=20', 'https://x.com/TheNCSmaster/status/1597726846460006400?s=20', 'https://x.com/IMDb/status/1597725655168610306?s=20', 'https://x.com/raiko_star/status/1598344553295142914?s=20', 'https://x.com/HeatherBearAMC/status/1597800196741935104?s=20', 'https://x.com/Mii_Mario_/status/1597731507426439168?s=20', 'https://x.com/Taiconan1/status/1597829836332216320?s=20', 'https://x.com/isaac_player42/status/1597715210428874753?s=20', 'https://x.com/megafan2001/status/1597716366898839553?s=20', 'https://x.com/JunpeiAnimates/status/1597719420566409216?s=20', 'https://x.com/cultofthelamb/status/1597728661561831425?s=20', 'https://x.com/Blun_Z/status/1597714608654929923?s=20', 'https://x.com/Valhallakingdom/status/1597714738812964864?s=20', 'https://x.com/sjfostersound/status/1597718828980400128?s=20', 'https://x.com/fewocious/status/1597719495790845952?s=20', 'https://x.com/artistgam3r/status/1597725622536925185?s=20', 'https://x.com/zezba9000/status/1600672439138390016?s=20', 'https://x.com/JamesFunsaBrown/status/1597786987582423042?s=20', 'https://x.com/ProjectLW1500/status/1597716543777144833?s=20', 'https://x.com/DrummerP94/status/1597725869434208257?s=20', 'https://x.com/BrianCHewson/status/1597729032149557249?s=20', 'https://x.com/krooked32/status/1597999689626177542?s=20', 'https://x.com/bandicootpage/status/1597715372446257152?s=20', 'https://x.com/kawaiiskull_nft/status/1597721171159846912?s=20', 'https://x.com/reitheboi/status/1597714813685469184?s=20', 'https://x.com/RevelXyz/status/1648685322362843138?s=20', 'https://x.com/qinggg__/status/1597715216623882241?s=20', 'https://x.com/Taiconan1/status/1597838931240050689?s=20', 'https://x.com/RealistMarc/status/1597831379395702784?s=20', 'https://x.com/OmerSideman/status/1648684199635824642?s=20', 'https://x.com/ToddPolker/status/1597729357350699008?s=20', 'https://x.com/Lynkronized/status/1597727917467119619?s=20', 'https://x.com/Lucafi0/status/1597714879536062464?s=20', 'https://x.com/nniro0999/status/1597715958587568128?s=20', 'https://x.com/i_slushee/status/1597714583031947265?s=20', 'https://x.com/carmineglitch/status/1597797995331784704?s=20', 'https://x.com/DespicableOutof/status/1597715790148472834?s=20', 'https://x.com/lazyjedi34/status/1597799263886508032?s=20', 'https://x.com/MisterManSandy/status/1597716901496750080?s=20', 'https://x.com/FORTL3GENDS/status/1597728453217775616?s=20', 'https://x.com/SPIDEY1500/status/1597717908020285440?s=20', 'https://x.com/emilio10001/status/1597743074473807872?s=20', 'https://x.com/Thibautst1/status/1597716397869580288?s=20']
    for link in links:
        append_json_to_file(parse.dict_to_json(scrape_tweet(link)))