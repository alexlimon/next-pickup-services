import requests
from app.services.helpers import parameter_validation
from app.services.clients import heb_client
from app.models.store_brand import StoreBrand
from queue import PriorityQueue
from datetime import datetime
import asyncio
import time

async def get_next_pickups(zipcode, num_stores_to_return = 5):
    if not await parameter_validation.is_zipcode_valid(zipcode):
        raise AttributeError("The zip code " + zipcode + " is invalid")

    heb = StoreBrand()
    heb.name = "HEB"
    heb.store_list = list()
    
    top_available_stores = await heb_client.get_stores_by_zipcode(zipcode)

    while not top_available_stores.empty() and num_stores_to_return > 0:
        heb.store_list.append(top_available_stores.get())
        num_stores_to_return -=1
        
    return heb