from dataclasses import dataclass
from dataclasses_json import dataclass_json
from datetime import datetime
from typing import List
from .store import Store

@dataclass_json
@dataclass(order = True, init = False)
class NotificationRecipient:
    last_notified: datetime = datetime.max
    created: datatime = datetime.now()
    phone_number: str
    zip_code: str
    verified: bool
    store_preferences: List[Store]
    