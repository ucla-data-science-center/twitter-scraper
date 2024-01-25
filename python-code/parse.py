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

def combine_words(words: list or str, **kwargs) -> str or list:
    res = ""
    if type(words) == list:
        res = []
        if (kwargs.get("method") == "OR" ):
            # FIXME
            for word in words:
                parsed = parse.quote(word)
                if (word != words[-1]):
                    parsed += "OR"
                res.append(parsed)
        elif (kwargs.get("method") == "AND"):
            # FIXME
            for word in words:
                parsed += parse.quote(word)
                if (word != words[-1]):
                    parsed += "AND"
                res.append(parsed)
        else:
            for word in words:
                res.append(parse.quote(word))
        return res
    else:
        res += parse.quote(words)
    return res

def hash_tags(str: list or str) -> str:
    return ""