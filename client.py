import os
from dotenv import load_dotenv
import tweepy

# loading environment variables
load_dotenv()

# Retrieving the Desired Variables.
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")


class Client:
    def __init__(self):
        """
        Initializes twitter client when an object is created.
        It needs to be an account which we will use for all our requests.
        """
        __client = tweepy.Client(
            bearer_token=BEARER_TOKEN,
            consumer_key=API_KEY,
            consumer_secret=API_KEY_SECRET,
            wait_on_rate_limit=True
        )    # creating the client that will be used for the access and requests


