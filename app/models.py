from pydantic import BaseModel
from typing import List


class ModelOutput(BaseModel):
    geo_h3_10: str
    model_type: str
    predictions: float


class ModelOutputResponse(BaseModel):
    data: List[ModelOutput]
