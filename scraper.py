import config
import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_TOKEN = config.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = config.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True)

saved_searches = api.saved_searches()

categories = [
    'Barack Obama'
]

analyzer = SentimentIntensityAnalyzer()
vaderOutput = open('vaderOutput.tsv', 'w')

vaderOutput.write('Tweet\\tPostive\\tNegative\\tNeutral\\tCompound\\n')

for search in saved_searches:
    saved_search = api.get_saved_search(search.id)
    print(str(saved_search.query))
    results = api.search(q=str(saved_search.query))
    print(results)
    # for result in results:
    #     print(result.text)
