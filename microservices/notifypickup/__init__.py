import datetime
import logging
import jsonpickle
import azure.functions as func
from ..core.services import text_notification_service
from ..core.services import manage_recipient_service

async def main(mytimer: func.TimerRequest) -> None:



