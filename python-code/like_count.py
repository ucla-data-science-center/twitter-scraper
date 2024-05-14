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

        follower_count = {}
        screen_name = set()
        relevant_likes = 0
        reply_count = 0
        retweet_count = 0
        favorite_count = 0
        quote_count = 0

        file_name = file.split("_filtered.json")[0]

        for i in data:
            relevant_likes += i['favorite_count']
            reply_count += i['reply_count']
            retweet_count += i['retweet_count']
            favorite_count += i['favorite_count']
            quote_count += i['quote_count']
            if i['screen_name'] not in screen_name:
                follower_count[i['screen_name']] = i['followers_count']

        print(json.dumps({
            "Movie": file_name, 
            "likes": relevant_likes, 
            "replies": reply_count,
            "retweets": retweet_count,
            "favorites": favorite_count,
            "quotes": quote_count,
            "follower_count": follower_count
        }))

def main():
    count_likes()
    return

if __name__ == "__main__":
    main()