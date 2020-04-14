from azure.storage import CloudStorageAccount
import os

class StorageAccount(CloudStorageAccount):
    def __init__(self):
        super().__init__(account_name = os.environ["STORAGE_ACCOUNT_NAME"], account_key=os.environ["STORAGE_ACCOUNT_KEY"])
