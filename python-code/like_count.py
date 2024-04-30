import os
import parse
import json

movie_titles = ['Transformers: Revenge of the Fallen:', 'Harry Potter and the Half-Blood Prince', 'The Twilight Saga: New Moon:', 'Avatar', 'Toy Story 3', 'Alice in Wonderland', 'Harry Potter and the Deathly Hallows: Part 2', 'Transformers: Dark of the Moon', 'The Twilight Saga: Breaking Dawn - Part 1', 'The Avengers', 'The Dark Knight Rises', 'The Hunger Games', 'Iron Man 3', 'The Hunger Games: Catching Fire', 'Despicable Me 2', 'Guardians of the Galaxy', 'Captain America: The Winter Soldier', 'Jurassic World', 'Avengers: Age of Ultron', 'Finding Dory', 'Beauty and the Beast', 'Wonder Woman', 'Black Panther', 'Avengers: Infinity War', 'Incredibles 2', 'Avengers: Endgame', 'The Lion King', 'Toy Story 4', 'Bad Boys for Life', 'Sonic the Hedgehog', 'Jumanji: The Next Level', 'Spider-Man: No Way Home', 'Shang-Chi and the Legend of the Ten Rings', 'Venom: Let There Be Carnage', 'Top Gun: Maverick', 'Black Panther: Wakanda Forever:', 'Doctor Strange in the Multiverse of Madness', 'Barbie', 'The Super Mario Bros. Movie', 'Spider-Man: Across the Spider-Verse:']

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

def count_likes():
    file_list = sorted(os.listdir('filtered_data/'))
    for file in file_list:
        data = read_json(f"filtered_data/{file}")

        relevant_likes = 0
        irrelevant_likes = 0

        file_name = file.split("_filtered.json")[0]

        for i in data:
            # for j in movie_titles:
            #     words = j.split(" ")
            #     lower =  j.lower().split(" ")
            #     for k in lower:
            #         words.append(k)
                
            #     print(words)
            relevant_likes += i['favorite_count']
        print(json.dumps({"Movie": file_name, "likes": relevant_likes}))

def main():
    count_likes()
    return

if __name__ == "__main__":
    main()