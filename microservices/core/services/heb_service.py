from .helpers import parameter_validation_async
from .clients import heb_client
from ..models.store import Store
from queue import PriorityQueue
from datetime import datetime
import asyncio
import time
from typing import List

async def get_next_pickups(zipcode, num_stores_to_return = 5, store_brand = None):
    
    await parameter_validation_async.validate_zipcode(zipcode)
    store_list: List[Store] = []

    top_available_stores = await heb_client.get_stores_by_zipcode(zipcode)

    while not top_available_stores.empty() and num_stores_to_return > 0:
        store_list.append(top_available_stores.get())
        num_stores_to_return -=1
        
    return store_list