from dataclasses import dataclass
from dataclasses_json import dataclass_json
from datetime import datetime

@dataclass_json
@dataclass(order = True, init = False)
class Store: 
    next_delivery_time: datetime = datetime.max
    next_pickup_time: datetime = datetime.max
    distance: int
    id: int
    name : str
    phone_number: str
    city: str
    state: str
    zipcode: str
    address: str
    store_hours: str
    store_brand: str
    location_link: str
    store_link: str


