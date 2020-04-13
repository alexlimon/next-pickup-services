from . import requests
from . import constants
async def is_zipcode_valid(zipcode):
    
    if(len(zipcode) < 5 or len(zipcode) > 5):
        raise  AttributeError("Not a valid zipcode: "+ zipcode)
  
    response = await requests.get_async(url= constants.USPS_VALIDATION_URL.format(ZIP = zipcode))

    if(len(response["addresses"]) < 1):
        return False
    
    return True

