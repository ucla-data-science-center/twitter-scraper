import json
from urllib import parse

def get_author(data: dict) -> str:
    core_data = data['core']
    


    return ""



def get_tweet(data: dict) -> str:
    legacy = data['legacy']
    return legacy['full_text']

def dict_to_json(data: dict) -> json:
    json_object = json.dumps(data, indent=4)
    return json_object

def combine_words(words: list or str, **kwargs) -> str:
    res = ""
    if type(words) == list:
        if (kwargs.get("method") == "OR" ):
            # FIXME
            for word in words:
                res += parse.quote(word)
                res += "OR"
        elif (kwargs.get("method") == "AND"):
            # FIXME
            for word in words:
                res += parse.quote(word)
                res += "AND"
        else:
            for word in words:
                res += parse.quote(word)
    else:
        res += parse.quote(words)
    return res

def hash_tags(str: list or str) -> str:
    return ""