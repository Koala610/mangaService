from pydantic import BaseModel
from typing import Optional

class Request(BaseModel):
    data: Optional[dict]