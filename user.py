from client import Client


class User(object):
    def __init__(self, username: str, password: str):     # might be initialized using the user's username and password
        pass

    def retrieve_search_keyword_data(self, keyword: str):
        """
        retrieves search data about this keyword from the Twitter API
        The 'Essential' access level allows only for retrieving search data from the past week
        :param keyword: the query to search for
        :return:
        """
        __new_client = Client()
        __new_client


    def display_data(self):
        pass
