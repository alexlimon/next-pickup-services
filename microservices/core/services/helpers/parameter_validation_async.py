from . import requests
from . import constants
import phonenumbers
import asyncio
import jsonpickle
from bson.json_util import loads, dumps

async def validate_zipcode(zipcode):
    
    if(len(zipcode) < 5 or len(zipcode) > 5):
        raise  AttributeError("The zip code " + zipcode + " is invalid")
  
    response = await requests.get_async(url= constants.USPS_VALIDATION_URL.format(ZIP = zipcode))

    if(len(response["addresses"]) < 1):
        raise AttributeError("The zip code " + zipcode + " is invalid")

async def validate_phone_number(phone_number_raw):
    loop = asyncio.get_running_loop()

    possible_phone_number = await loop.run_in_executor(None, phonenumbers.parse, phone_number_raw, "US")
    is_valid_number = await loop.run_in_executor(None, phonenumbers.is_valid_number, possible_phone_number)

    if not is_valid_number:
        raise AttributeError(phone_number_raw + " is not a valid phone number! Try again with a different number.")

async def custom_object_to_dict(custom_object):
    loop = asyncio.get_running_loop()

    json_encoded_object = await loop.run_in_executor(None, jsonpickle.encode, custom_object)
    dict_encoded_object = await loop.run_in_executor(None, loads, json_encoded_object)

    return dict_encoded_object

async def dict_to_custom_objects(dict_object, list_of_custom_object = None):
    loop = asyncio.get_running_loop()

    json_object = await loop.run_in_executor(None, dumps, dict_object)
    recipient = await loop.run_in_executor(None, jsonpickle.decode, json_object)

    if list_of_custom_object is not None:
        list_of_custom_object.append(recipient)

    return recipient

    
