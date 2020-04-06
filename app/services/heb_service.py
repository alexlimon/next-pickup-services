import requests
from app.services.helpers import parameter_validation
from app.services.clients import heb_client
from app.models.store_brand import StoreBrand
from queue import PriorityQueue
from datetime import datetime
import asyncio
import time

async def get_next_pickups(zipcode):
    if not await parameter_validation.is_zipcode_valid(zipcode):
        raise AttributeError("The zip code " + zipcode + " is invalid")
    
    heb = StoreBrand()
    heb.name = "HEB"
    heb.store_list = list()
    
    all_stores = await heb_client.get_stores_by_zipcode(zipcode)

    top_available_stores = PriorityQueue()

    for store in all_stores:
        queue_task = asyncio.create_task(populate_queue_with_stores(store, top_available_stores))
    
    await queue_task

    total_stores = top_available_stores.qsize()
    num_of_stores_to_return = 5

    while not top_available_stores.empty() and top_available_stores.qsize() > total_stores - num_of_stores_to_return:
        heb.store_list.append(top_available_stores.get())

    return heb

async def populate_queue_with_stores(store, top_available_stores):
    earliest_pickup_date = await heb_client.get_earliest_pickup_day(store.id)
    
    if earliest_pickup_date is not None:
        store.next_pickup_time = datetime.strptime(earliest_pickup_date,'%Y-%m-%dT%H:%M:%S')
        top_available_stores.put(store)