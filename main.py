import streamlit as sl
from client import Client

test_client = Client()
response = test_client.retrieve_search_keyword_data("nft")
print(response)







