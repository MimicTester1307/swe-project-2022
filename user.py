from data import DATA
import pandas as pd
import streamlit as st


class User:
    def __init__(self):
        pass

    # def get_data(self, query):
    #     """
    #     minimizes call to API endpoint by calling data retrieval function once
    #     then returning the data for display functions to use
    #     :param query: the query to search for
    #     :return: Response data
    #     """
    #     data = retrieve_search_keyword_data(query=query)
    #     return data

    def display_data(self, data=DATA):
        """
        visualizes the retrieved data as a line chart using streamlit
        :return: None
        """

    def normalize_data(self, data):
        pass


