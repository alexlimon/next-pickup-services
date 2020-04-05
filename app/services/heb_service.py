import requests
from app.services.helpers import parameter_validation
from app.services.clients import heb_client
from app.models.store_brand import StoreBrand
from queue import PriorityQueue
from datetime import datetime
import time

def get_next_pickups(zipcode):
    
    start_time = time.time()

    if not parameter_validation.is_zipcode_valid(zipcode) :
        raise AttributeError("The zip code " + zipcode + " is invalid")

    heb = StoreBrand()
    heb.name = "HEB"
    heb.store_list = list()

    setup_time = time.time()

    all_stores = heb_client.get_stores_by_zipcode(zipcode)
    
    allstores_time = time.time()

    top_available_stores = PriorityQueue()

    for store in all_stores:
        earliest_pickup_date = heb_client.get_earliest_pickup_day(store.id)

        if earliest_pickup_date is not None:
            store.next_pickup_time = datetime.strptime(earliest_pickup_date,'%Y-%m-%dT%H:%M:%S')
            top_available_stores.put(store)
    
    while not top_available_stores.empty and top_available_stores.qsize() > top_available_stores.qsize() - 5:
        heb.store_list.append(top_available_stores.get())

    return heb

