
import requests
import tweepy
import os
import webbrowser
##############################################################
# UNFORTUNATELY V2 API ARE LIMITED WITH FREE ACCOUNT
# NO SEARCH ALLOWED
# SO STOPPING HERE..
#############################################################
# Example to test Full oauth authentication
print("This requires at least TW_ACCESS_TOKEN and TW_ACCESS_TOKEN_SECRET")
print("to be defined as env vars")
print("Check file: tiwtter_token in main folder")
consumer_key = os.environ['TW_ACCESS_TOKEN']
consumer_secret = os.environ['TW_ACCESS_TOKEN_SECRET']


if os.environ.get('TW_SESSION_ACCESS_TOKEN') == None or \
   os.environ.get('TW_SESSION_ACCESS_TOKEN_SECRET') == None:
    #
    # we need to visit the url to get a pin code; this is MFA based
    # so human interaction is required    
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret,callback="oob")
    url = auth.get_authorization_url()
    print(f"Now visiting {url} to get the PIN code")
    webbrowser.open(url)

    verifier = input("Input PIN: ")
    ACCESS_TOKEN, ACCESS_TOKEN_SECRET = auth.get_access_token(verifier)

else:  
    print("Getting session tokens from ENV vars")
    ACCESS_TOKEN = os.environ['TW_SESSION_ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = os.environ['TW_SESSION_ACCESS_TOKEN_SECRET']  


print(f"CONSUMER KEY: {consumer_key}\nCONSUMER_SECRET {consumer_secret}")
print(f"ACCESS_TOKEN: {ACCESS_TOKEN}\nACCESS_TOKEN_SECRET {ACCESS_TOKEN_SECRET}")
#
# set the remaining parts 
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
#
# test getting my own info
twitter_name='e18hn'
user = api.get_user(screen_name=twitter_name)
print(f"User id for {twitter_name} is {user.id}")
print(f"User description for {twitter_name} is {user.description}")
print(f"User location for {twitter_name} is {user.location}")

#
# function to get tweets
def get_tweets(api, query, count = 300):
    """
    This method will return a list of tweets matching query
      api  : is the twitter api object
      query: query to filter
      count: number of twitter (max) to retrieve, default is 300
    """

    # empty list to store parsed tweets
    tweets = []
    # call twitter api to fetch tweets
    q=str(query)
    fetched_tweets = api.search_tweets(q, count = count)
    # parsing tweets one by one
    print(len(fetched_tweets))

    return tweets

# creating object of TwitterClient Class
# calling function to get tweets
# well it seems that v2 apis are also limited and lookup
print("calling APis to get tweets..")
tweets = get_tweets(api, query ="data science", count = 20)
for tweet in tweets:
    user = tweet["user"]["screen_name"]
    text = tweet["text"]
    print("-------------------")
    print(f"--- user: {user}")
    print(f"--- text: {text}")    
    print(f"Full tweet:\n{tweet}")