import os
import parse
import json

def read_json(path: str) -> list:
    res = []
    f = open(path)
    data = json.load(f)
    
    # Iterating through the json
    # list
    for i in data:
        res.append(i)
    # Closing file
    f.close()
    return res

def filter():
    file_list = os.listdir('./')
    ordered_list = [file for file in file_list if "ordered.json" in file]
    for file in ordered_list:
        print(file)

        data = read_json(f"./{file}")
        filed_name = file.split("ordered.json")[0]

        if (f"{filed_name}_filtered.json" in file_list):
            continue

        for i in data:
            new_dict = {}
            new_dict['rest_id'] = i['rest_id']
            new_dict['created_at'] = i['core']['user_results']['result']['legacy']['created_at']
            new_dict['followers_count'] = i['core']['user_results']['result']['legacy']['followers_count']
            new_dict['name'] = i['core']['user_results']['result']['legacy']['name']
            new_dict['screen_name'] = i['core']['user_results']['result']['legacy']['screen_name']
            new_dict['favorite_count'] = i['legacy']['favorite_count']
            new_dict["quote_count"] = i['legacy']['quote_count']
            new_dict["reply_count"] = i['legacy']['reply_count']
            new_dict["retweet_count"] = i['legacy']['retweet_count']
            new_dict['full_text'] = i['legacy']['full_text']
            with open(f"filtered_data/{filed_name}_filtered.json", 'a') as outfile:
                    json_object = json.loads(json.dumps(parse.dict_to_json(new_dict)))
                    outfile.write(json_object)
                    outfile.write(",\n")


    return file_list

def main():
    filter()
    return

if __name__ == "__main__":
    main()