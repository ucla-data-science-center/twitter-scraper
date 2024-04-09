import os
import parse
import json
import pandas as pd

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

def to_csv():
    file_list = os.listdir('data/collected_data')
    file_list = os.listdir('data/collected_data')
    filtered_list = [file for file in file_list if "_filtered.json" in file]

    for i in filtered_list:
        # Sample JSON data (list of dictionaries)
        json_data = read_json(f"data/collected_data/{i}")

        # Convert JSON data to a pandas DataFrame
        df = pd.DataFrame(json_data)

        file_name = i.split("_filtered")[0]

        # Specify the file path for your CSV file
        csv_file_path = f"data/collected_data/{file_name}.csv"

        # Write the DataFrame to a CSV file
        df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')


    return file_list

def main():
    to_csv()
    return

if __name__ == "__main__":
    main()