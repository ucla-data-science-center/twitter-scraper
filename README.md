# Twitter/X Scraper

The code in this repository aims to be able to help you scrape tweets. It scrapes tweets by filling out several parameters that you can use.
It essentially takes in the parameters you can input in the advanced search option on twitter and will look up tweets according to that.

## Getting Started

### Signing In
First you must create a .env file inside of the python-code folder. Inside this .env file you will fill out the following parameters with your UCLA SSO information:
```
UCLA_LOGON=""
UCLA_PASSWORD=""
UCLA_EMAIL=""
```
Currently the only way to use this tool is through a google sign-in with a UCLA SSO. This is currently a work in progress and hope to expand to other sign-in methods.

### Search Data
Now, you need to populate the master_list.json file in the data folder. You can find an example of what a search looks like in the example/master_list.json file. You can add other parameters such as hashtags and other parameters that are present in X's advanced search. 

Example Search:
```
{
     "Keyword": "The Dark Knight",
     "Hashtags": "#batman, #theDarkKnight,"
     "Twitter Accounts (that exist)": "@TheOfficialBale, @themichaelcaine",
     "Start Date": "December 14, 2007",
     "End Date": "December 9, 2008"
},
```

Now copy the data from the master_list.json file and paste it into the search.json file. This file is used for the searching algorithm and you will alter this as you search and scrape tweets.

### Running the Code

You first want to scrape individual links before you gather the content. Run the following command:
```
python3 python-code/main.py
```
The ***main.py*** file will first log you into twitter then scrape the links to the tweets based on the searches you have inputed in the search.json file. The links that are collected will go into links.txt. Every once in awhile pay attention to the script, it may run into an <span style="color: #2E49A9">RETRY</span> error. When you encounter this error stop the script and wait a few minutes before re-running the script. You should remove any of the searches that were successful from the search.json file prior to re-running the script.

After collecting the links you want to scrape. Go to links.txt and copy a single list of links. Input that list into the ***links*** array in the scrape_tweets.py. After filling in the array. Run the following command to scrape the tweets:
```
python3 python-code/scrape_tweets.py
```
Again, watch the script every once in awhile in case it runs into a <span style="color: #2E49A9">RETRY</span> error. If it does, look at the latest scraped tweet and remove all of the tweets prior from it from the ***links*** array.

Once you have scraped the tweets, run:
```
python3 python-code/conversion.py
```
This script will convert your unordered json file into a proper json file and then you can rename your files to what you want.

<span style="color:#DB4848"> ***NOTE***: Make sure to rename your unordered.json and ordered.json files that are in your data/collected_data folder. If you do not, the scraped tweets will all be appended to one file and you won't be able to differentiate between the search terms.
</span> 

<h2 style="color: #DB4848;"> Limitations </h2>
<p style="color: #DB4848;">
There are several limitations to this tool. It may run into issues of being unable to load and collect tweets because of the anti-scraping techniques
employed by X. Please be aware of that and proceed with that knowledge and the fact that it won't scrape the same tweets every single time. It may also scrape advertisements as well. This methodology works most effectively for collecting specific data from accounts or searches. It does not work in the general case. It will also not collect millions of data points.
</p>