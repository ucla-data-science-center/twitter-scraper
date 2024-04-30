import os
import parse
import json

def read_json(path: str) -> list:
    results = []
    with open(path, 'r') as file:
        for line in file:
            # Attempt to parse each line as a JSON object
            try:
                data = json.loads(line)
                results.append(data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from line: {line}")
                print(f"Error: {e}")
    return results

def count_likes():
    file_list = os.listdir('data_2/collected_data')
    ordered_list = [file for file in file_list if "_ordered.json" in file]
    for file in ordered_list:
        print(file)

        data = read_json(f"data_2/collected_data/{file}")
        filed_name = file.split("_ordered.json")[0]

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

def main():
    count_likes()
    return

if __name__ == "__main__":
    main()