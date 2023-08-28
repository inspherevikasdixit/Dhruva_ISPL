from typing import Any, Dict, Optional

from pydantic import BaseModel

from .ulca_base_inference_request_config import _ULCABaseInferenceRequestConfig
from .ulca_control_config import _ControlConfig


class _ULCABaseInferenceRequest(BaseModel):
    controlConfig: _ControlConfig = _ControlConfig()
    config: _ULCABaseInferenceRequestConfig

    def set_service_id(self, service_id: str):
        self.config.serviceId = service_id
