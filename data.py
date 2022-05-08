from client import Client

# Initializing Client
test_client = Client().get_client()


# This method will retrieve the tweet counts
# for the searched keyword
def retrieve_tweet_count_data(query: str):
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

    response = test_client.get_recent_tweets_count(query=query, granularity="day")

    return response.data


# This method will retrieve the tweet likes
# and comments to measure engagement
def populate_count_array(query: str):
    count_array = []
    count_data = retrieve_tweet_count_data(query)
    for data in count_data:
        count_array.append(data["tweet_count"])

    return count_array


# TODO: this throws an error, check pandas
#  documentation in project Notion page on how to change orient parameter
# test_dict = json.loads(DATA)
# test_df = pd.json_normalize(test_dict)
# print(test_df)

# TODO: Add function to retrieve number of likes for tweets and maybe number of comments; to measure engagement
