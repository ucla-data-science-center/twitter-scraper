import json
from urllib import parse

months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

def convert_to_date(date: str) -> str:
    date = date.split()
    month_number = 1
    for i in months:
        if i != date[0]:
            month_number += 1
        else:
            break
    return f"{date[2]}-{month_number}-{date[1].replace(',', '')}"

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