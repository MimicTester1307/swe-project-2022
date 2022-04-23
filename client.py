import os
from dotenv import load_dotenv
import tweepy
import json


# loading environment variables
load_dotenv()

# Retrieving the Desired Variables.
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")


class Client:
    def __init__(self):
        """
        Initializes twitter client when an object is created.
        It needs to be an account which we will use for all our requests.
        """
        self.__client = tweepy.Client(
            bearer_token=BEARER_TOKEN,
            consumer_key=API_KEY,
            consumer_secret=API_KEY_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET,
            wait_on_rate_limit=True
        )    # creating the client that will be used for the access and requests

    def retrieve_search_keyword_data(self, keyword: str):
        """
        retrieves search data about this keyword from the Twitter API
        The 'Essential' access level allows only for retrieving search data from the past week
        :param keyword: the query to search for
        :return: Response data
        """
        response = self.__client.search_recent_tweets(
            query=keyword,
            max_results=10,
            expansions=["geo.place_id"],
            tweet_fields=["context_annotations",    # entity recognition/extraction, topical analysis
                          "created_at",    # to understand when Tweet was created and used for time-series analysis
                          "public_metrics"    # to measure tweet engagement
                          ],
            place_fields=["country"]
        )

        return response.json()

    def display_data(self):
        pass


