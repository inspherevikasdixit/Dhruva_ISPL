from typing import Optional

from pydantic import BaseModel

from ..common import _ULCATaskType, _ULCATextPair, _ULCATranslationInferenceConfig


class ULCATranslationInferenceResponse(BaseModel):
    taskType: _ULCATaskType = _ULCATaskType.TRANSLATION
    output: list[_ULCATextPair]
    config: Optional[_ULCATranslationInferenceConfig]
