from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from datetime import datetime
from typing import List
from .store_brand import StoreBrand
from ..services.helpers import parameter_validation_async
from phonenumbers import phonenumber, is_valid_number, parse

@dataclass_json
@dataclass(order = True, init = True)
class NotificationRecipient:
    _id: str = field(init = False)
    last_notified: datetime = field(init=False)
    created: datetime = field(init=False)
    phone_number: str 
    zipcode: str 
    name: str
    verified: bool = field(init=False)
    store_preferences: List[StoreBrand] = field(init=False)
 
    def __post_init__(self):
        self.verified = False
        self.created = datetime.now()
        self.last_notified = datetime.max

    async def validate_properties_async(self):  
        await parameter_validation_async.validate_phone_number(self.phone_number)
        await parameter_validation_async.validate_zipcode(self.zipcode)
        
        if self.name is None:
            raise AttributeError("Name cannot be none")

