import pytest
import requests
import os
from dotenv import load_dotenv
import tweepy

# loading environment variables
load_dotenv()

# Retrieving the Desired Variables.
TEST_BEARER_TOKEN = os.getenv("BEARER_TOKEN")
TEST_API_KEY = os.getenv("API_KEY")
TEST_API_KEY_SECRET = os.getenv("API_KEY_SECRET")
TEST_ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
TEST_ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

def test_client():
    pass
