# we'll use twitter's streaming API  in particular we'll use the public
# stream wich streams of the public data flowing through twitter

# We'll use the get status/sample API wich returns random sample
# of all public statuses  

# Tweets are returned as JSONS and they containg numerous possible fields

# Using tweepy: Authentication
# This library has a nice balance of usability and capability
import tweepy, json

# Create Streaming object
stream = tweepy.Stream(consumer_key, consumer_secret,
                       access_token, access_token_secret)

# This line filters Twitter Streams to capture data by keywords:
stream.filter(track=['apples', 'oranges'])

import json

# Define the path to your local file
tweets_data_path = 'tweets.txt'

# Initialize empty list to store tweets
tweets_data = []

# Open connection to file
with open(tweets_data_path, "r") as tweets_file:
    # Read in tweets and store in list
    for line in tweets_file:
        tweet = json.loads(line)
        tweets_data.append(tweet)

# Now you can print keys just like in the course!
print(tweets_data[0].keys())
