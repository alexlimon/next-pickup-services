from . import requests

async def is_zipcode_valid(zipcode):
    
    if(len(zipcode) < 5 or len(zipcode) > 5):
        raise  AttributeError("Not a valid zipcode: "+ zipcode)

    USPS_VALIDATION_URL = "https://m.usps.com/m/QuickZipAction?mode=2&tZip={ZIP}&jsonInd=Y"
    
    response = await requests.get_async(url= USPS_VALIDATION_URL.format(ZIP = zipcode))

    if(len(response["addresses"]) < 1):
        return False
    
    return True
