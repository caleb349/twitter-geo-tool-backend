# Import Packages
import tweepy
from geopy import Nominatim

# Create Credential Keys
consumer_key = 'V6XKhulVp7YYY3jVJAE5yZHcR'
consumer_secret = 'k6ydihnwe2Oue1ITswLVTSHrD5YpLQyNIQlWrxlLnvBYwjRFuL'
access_token = '2620473211-yUybtaw3CDNd9vyHh9qSvgOul1pkiOuB0wpVEts'
access_token_secret = 'srxKoqEdF0SJbBnB8K2mgcz1m7AOJLUVHofIB5yyycXAZ'

# Set Up Configuration
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Fetching Government & Politics Trends
def get_politics(location_selected):
    # Define the search term and the date_since date as variables
    query = "election -filter:retweets"  # removes retweets
    date_since = '2020/01/01'

    # Collect tweets
    tweets = tweepy.Cursor(api.search,
                           q=query,
                           since=date_since,
                           geocode=location_selected,
                           lang="en",
                           ).items(10)

    # Print tweets and attached attributes
    tweet_obj = []
    for tweet in tweets:
        users_attributes = [tweet.user.screen_name, tweet.user.location, tweet.text]
        tweet_obj.append(users_attributes)
    return(tweet_obj)


# Fetching Food Trends
def get_food(location_selected):
    # Define the search term and the date_since date as variables
    query = "food -filter:retweets"  # removes retweets
    date_since = '2020/07/01'

    # Collect tweets
    tweets = tweepy.Cursor(api.search,
                           q=query,
                           date_since=date_since,
                           geocode=location_selected,
                           lang="en",
                           ).items(10)

    # Print tweets and attached attributes
    tweet_obj = []
    for tweet in tweets:
        users_attributes = [tweet.user.screen_name, tweet.user.location, tweet.text]
        tweet_obj.append(users_attributes)
    return(tweet_obj)

# Fetching Pop Culture Trends
def get_pop_culture(location_selected):
    # Define the search term and the date_since date as variables
    query = "tiktok+youtube -filter:retweets"  # removes retweets
    date_since = '2020/07/01'

    # Collect tweets
    tweets = tweepy.Cursor(api.search,
                           q=query,
                           date_since=date_since,
                           geocode=location_selected,
                           lang="en",
                           ).items(10)

    # Print tweets and attached attributes
    tweet_obj = []
    for tweet in tweets:
        users_attributes = [tweet.user.screen_name, tweet.user.location, tweet.text]
        tweet_obj.append(users_attributes)
    return(tweet_obj)

# Fetching Technology Trends
def get_technology(location_selected):
    # Define the search term and the date_since date as variables
    query = "tech -filter:retweets"  # removes retweets
    date_since = '2020/07/01'

    # Collect tweets
    tweets = tweepy.Cursor(api.search,
                           q=query,
                           date_since=date_since,
                           geocode=location_selected,
                           lang="en",
                           ).items(10)

    # Print tweets and attached attributes
    tweet_obj = []
    for tweet in tweets:
        users_attributes = [tweet.user.screen_name, tweet.user.location, tweet.text]
        tweet_obj.append(users_attributes)
    return(tweet_obj)

# Fetching Latest Tweets
def get_latest(location_selected):
    # Define the search term and the date_since date as variables
    query = "-filter:retweets"  # removes retweets
    date_since = '2020/07/01'

    # Collect tweets
    tweets = tweepy.Cursor(api.search,
                           q=query,
                           date_since=date_since,
                           geocode=location_selected,
                           lang="en",
                           ).items(10)

     # Print tweets and attached attributes
    tweet_obj = []
    for tweet in tweets:
        users_attributes = [tweet.user.screen_name, tweet.user.location, tweet.text]
        tweet_obj.append(users_attributes)
    return(tweet_obj)
