from client import Client
import json
import pandas as pd


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
    # Initializing Client
    test_client = Client().get_client()

    response = test_client.get_recent_tweets_count(query=query, granularity="day")

    return response.data


# Retrieved data
DATA = retrieve_search_keyword_data("nft #nft")
# TODO: this throws an error, check pandas
#  documentation in project Notion page on how to change orient parameter
test_dict = json.loads(DATA)
test_df = pd.json_normalize(test_dict)
print(test_df)
