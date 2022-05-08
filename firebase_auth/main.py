import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
from data import populate_count_array


# DOCUMENT IDs
DOCUMENT_IDS = ["MVFEnZf4hzWZOcgf1qWh", "PgAcH7Y6rKkxWeQRLiUr", "RlJLxrEi1zzAsRIppL0o", "VdDASBx2E6XNf5Ta0f4n",
                "XDrra8AIJkFGkp4ZXcpD", "hrkUFcby00let312ejxS", "liUJnSEoFU2wZVYjtt7M", "oTdWBtxjbc9d1Gjyc8Y7",
                "qYX2Gj9NCSh9pk6gF7Qk", "zaAkEe62zvTO0ynUNyYC"
                ]

# FIRESTORE CREDENTIALS
cred = credentials.Certificate("nft-project-ac35e-firebase-adminsdk-ujo8c-b728fbcc08.json")
app = firebase_admin.initialize_app(cred)

# Initializing the client and retrieving
firestore_client = firestore.client()

# Updating document with Twitter count
# TODO: In the future, we will improve the code to run asynchronously
for ID in DOCUMENT_IDS:
    doc_ref = firestore_client.document(f"collections/{ID}")

    try:
        # Retrieving the Tweet Data using the column name in firestore
        query_dict = doc_ref.get(field_paths={u'col_name'}).to_dict()
    except google.cloud.exceptions.NotFound:
        print(u"Missing Data")

    query = query_dict["col_name"]    # since the data is returned as a dictionary, the actual query needs to
    # be extracted from it

    # Searching for tweet count data on Twitter and storing them in firestore
    tweet_count_data = populate_count_array(query=query)    # searching and retrieving the tweet count
    doc_ref.update(field_updates={"tweet_count": tweet_count_data})    # updating the firestore database
