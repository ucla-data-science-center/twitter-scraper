import json

def conversion():
    with open("./data/collected_data/unordered.json", 'r') as file:
        for line in file.readlines():
            bruh = json.loads(line)
            with open("./data/collected_data/ordered.json", "a") as outfile:
                outfile.write(bruh)
                outfile.write(',')
                outfile.write("\n")

if __name__ == "__main__":
    conversion()