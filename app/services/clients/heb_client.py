from app.services.helpers import requests
import json
from app.models.store import Store

HEB_BASE_URL = "https://www.heb.com/commerce-api/v1/"

def get_stores_by_zipcode(zipcode, radius = 10, curbside_only = True, next_available_timeslot = True):
    
    heb_stores = []

    request_payload = {"address": zipcode, "curbsideOnly": curbside_only, "radius": radius, "nextAvailableTimeslot": next_available_timeslot}
    
    response = requests.post(HEB_BASE_URL + "store/locator/address", json.dumps(request_payload))

    for response_obj in response["stores"]:
        new_store = Store()
        add_properties_to_store(new_store, response_obj["store"])
        heb_stores.append(new_store)
    
    return heb_stores

def get_earliest_pickup_day(store_id, num_days_to_check = 30):
    timeslot_query = "timeslot/timeslots?store_id={store_id}&days={num_days}&fulfillment_type=pickup"
    response = requests.get(HEB_BASE_URL + timeslot_query.format(store_id = store_id, num_days = str(num_days_to_check)))
    
    if response["items"] is None or len(response["items"]) < 1:
        return None
    return response["items"][0]["timeslot"]["startTime"][:19]


def add_properties_to_store(store, response_dict):
    store.name = response_dict["name"]
    store.city = response_dict["city"]
    store.address = response_dict["address1"]
    store.phone_number = response_dict["phoneNumber"]
    store.id = int(response_dict["id"])
    store.zipcode = response_dict["postalCode"][:5]
    store.location_link = "https://www.google.com/maps/search/?api=1&query={lat},{long}".format(lat = response_dict["latitude"], long = response_dict["longitude"])
    store.store_hours = response_dict["storeHours"]
    store.state = response_dict["state"]







	
