from typing import Optional
from pydantic import BaseModel


class AISchema(BaseModel):
    proxy: str
    url: str
    header: Optional[str] = "--header ''"