from client import Client
import json
import pandas as pd

# Initializing Client
__client = Client()
CLIENT = __client.get_client()


# This method will be static to minimize function calls
# and stay within the rate limit
def retrieve_search_keyword_data(query: str):
    """
    retrieves search data about this keyword from the Twitter API
    The 'Essential' access level allows only for retrieving search data from the past week
    :param query: the query to search for
    :return: Response data
    """
    # response = self.__client.search_recent_tweets(
    #     query=keyword,
    #     max_results=10,
    #     expansions=["geo.place_id"],
    #     tweet_fields=["context_annotations",    # entity recognition/extraction, topical analysis
    #                   "created_at",    # to understand when Tweet was created and used for time-series analysis
    #                   "public_metrics"    # to measure tweet engagement
    #                   ],
    #     place_fields=["country"]
    # )
    client = CLIENT.get_client()
    response = client.get_recent_tweets_count(query=query, granularity="hour")

    return response.data


# Retrieved data
DATA = retrieve_search_keyword_data("nft #nft")

test_dict = json.loads(DATA)
test_df = pd.json_normalize(test_dict)
print(test_df)
