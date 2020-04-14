import datetime
import logging
import azure.functions as func
from azure.storage import CloudStorageAccount
from azure.storage.table import TableService, Entity
from ..core.services.helpers import notification_table_operations

def main(mytimer: func.TimerRequest) -> None:
    notification_table_operations.get_all_recipients()