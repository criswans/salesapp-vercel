from pydantic import BaseModel
from typing import Optional

class task_schema(BaseModel):
   Name :str
   Owner :str

   class Config:
       orm_mode = True