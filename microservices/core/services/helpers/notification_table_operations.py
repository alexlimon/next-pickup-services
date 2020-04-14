from .providers import storage_account_provider
from azure.storage.table import TableService, Entity
from . import constants
import datetime
import os


table_service = storage_account_provider().create_table_service()

notification_rec = table_service.query_entities(constants.NOTIFICATION_TABLE_NAME)

async def get_all_recipients():
    for rec in notification_rec:
        print(rec)
    return

async def insert_recipient(new_recipient):
    return

async def delete_recipient(new_recipient):
    return

async def get_recipients_to_notify():
    return

