from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from .store import Store
from typing import List

@dataclass_json
@dataclass (order = True, init = False)
class StoreBrand:
    name: str
    store_list: List[Store] 