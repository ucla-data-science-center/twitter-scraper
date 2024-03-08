import os
import parse
import json

def append_json_to_file(json_obj):
    """Append a JSON object to a file."""
    with open("./data/unordered.json", 'a') as file:
        # Convert JSON object to string and write it to file
        # json_string = json.dumps(json_obj) + "\n"
        # print(json_string)
        file.write(json.dumps(json_obj) + "\n")

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
    file_list = os.listdir('data/collected_data')
    ordered_list = [file for file in file_list if "_ordered.json" in file]
    for file in ordered_list:
        data = read_json(f"data/collected_data/{file}")
        filed_name = file.split("_ordered.json")[0]

        if (f"{filed_name}_filtered.json" in file_list):
            continue

        for i in data:
            new_dict = {}
            new_dict['rest_id'] = i['rest_id']
            new_dict['like_count'] = i['legacy']['favorite_count']
            new_dict["quote_count"] = i['legacy']['quote_count']
            new_dict["reply_count"] = i['legacy']['reply_count']
            new_dict["retweet_count"] = i['legacy']['retweet_count']
            new_dict['bookmark_count'] = i['legacy']['bookmark_count']
            new_dict['content'] = i['legacy']['full_text']
            new_dict['hashtags'] = i['legacy']['entities']['hashtags']
            with open(f"data/collected_data/{filed_name}_filtered.json", 'a') as outfile:
                    json_object = json.loads(json.dumps(parse.dict_to_json(new_dict)))
                    outfile.write(json_object)
                    outfile.write(",\n")


    return file_list

def main():
    filter()
    return

if __name__ == "__main__":
    main()