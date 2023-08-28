from typing import Optional

from pydantic import BaseModel


class _ULCABaseInferenceRequestConfig(BaseModel):
    serviceId: str = ""

    class Config:
        extra = "allow"
