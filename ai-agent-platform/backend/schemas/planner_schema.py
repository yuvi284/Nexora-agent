from pydantic import BaseModel
from typing import List

class PlannerOutput(BaseModel):
    tasks: List[str]