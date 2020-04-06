from app.services.helpers import requests
import json
from app.models.store import Store
import asyncio
import time
HEB_BASE_URL = "https://www.heb.com/commerce-api/v1/"

async def get_stores_by_zipcode(zipcode, radius = 10, curbside_only = True, next_available_timeslot = True): 
    heb_stores = []

    request_payload = {"address": zipcode, "curbsideOnly": curbside_only, "radius": radius, "nextAvailableTimeslot": next_available_timeslot}

    response = await requests.post_async(HEB_BASE_URL + "store/locator/address", json.dumps(request_payload))
    
    for response_obj in response["stores"]:
       populate_store_task = asyncio.create_task(create_and_append_store(response_obj["store"], heb_stores))
    
    await populate_store_task

    return heb_stores

async def get_earliest_pickup_day(store_id, num_days_to_check = 30):
    timeslot_query = "timeslot/timeslots?store_id={store_id}&days={num_days}&fulfillment_type=pickup"

    response = await requests.get_async(HEB_BASE_URL + timeslot_query.format(store_id = store_id, num_days = str(num_days_to_check)))
    
    if response["items"] is None or len(response["items"]) < 1:
        return None
    return response["items"][0]["timeslot"]["startTime"][:19]


async def create_and_append_store(response_dict, heb_stores):
    new_store = Store()

    new_store.name = response_dict["name"]
    new_store.city = response_dict["city"]
    new_store.address = response_dict["address1"]
    new_store.phone_number = response_dict["phoneNumber"]
    new_store.id = int(response_dict["id"])
    new_store.zipcode = response_dict["postalCode"][:5]
    new_store.location_link = "https://www.google.com/maps/search/?api=1&query={lat},{long}".format(lat = response_dict["latitude"], long = response_dict["longitude"])
    new_store.store_hours = response_dict["storeHours"]
    new_store.state = response_dict["state"]

    heb_stores.append(new_store)







	
