import os
import pymongo
from azure.storage import CloudStorageAccount

def provide_storage_account():
    return CloudStorageAccount(account_name = os.environ["STORAGE_ACCOUNT_NAME"], account_key = os.environ["STORAGE_ACCOUNT_KEY"])

def provide_db_connection():
    cosmos_db_client = pymongo.MongoClient(os.environ["MONGO_CONNECTION_STRING"])
    return cosmos_db_client.next_grocery_storage