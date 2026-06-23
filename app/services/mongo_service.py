from pymongo import MongoClient
import os
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]

 
def get_document(collection_name, filter_query):
    collection = db[collection_name]
    return collection.find_one(filter_query)
# # def get_document(collection_name, filter_query):
# #     """
# #     Get a single document from MongoDB
# #     """
# #     collection = db[collection_name]
# #     return collection.find_one(filter_query)
 
# #  from database import db
# # from utility.decrypt import decrypt

# # def get_document(collection_name, filter_query):
# #     collection = db[collection_name]
# #     return collection.find_one(filter_query)


# from database import db
# from utility.decrypt import decrypt

# def get_document(collection_name, filter_query):
#     collection = db[collection_name]
#     return collection.find_one(filter_query)


# def get_api_key(collection_name, filter_query):
#     doc = get_document(collection_name, filter_query)

#     if not doc:
#         return None

#     encrypted_key = doc.get("Security")

#     if not encrypted_key:
#         return None

#     return decrypt(encrypted_key)