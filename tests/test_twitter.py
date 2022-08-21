import tweepy
from twitter_api_interactions.client import Client
from twitter_api_interactions import data

test_client_object = Client().get_client()


def test_get_client():
    """
    simple test case for the Client object.
    tests if the client is actually returned after being created by checking its type
    :return: None
    """
    assert type(test_client_object) is tweepy.client.Client


def test_retrieve_tweet_count_data(test_query: str = "BAYC"):
    """
    simple test case for retrieving tweet count data
    tests if the response is in the right format and the needed key is in the returned data objects
    :param test_query:
    :return: response data
    """
    test_response = test_client_object.get_recent_tweets_count(query=test_query, granularity="day")
    assert all([type(datum) is dict for datum in test_response.data]) and \
           all(["tweet_count" in datum for datum in test_response.data])
    return test_response.data


def test_populate_count_array(test_query: str = "Okay Bears #NFT"):
    """
    simple test case for checking if the array to be sent to the firestore database is in the right format:
    an array or list of integers.
    :param test_query:
    :return: None
    """
    test_count_array = []
    test_count_data = test_retrieve_tweet_count_data(test_query)
    for test_data in test_count_data:
        test_count_array.append(test_data["tweet_count"])

    assert type(test_count_array) is list and all([type(count) is int for count in test_count_array])
