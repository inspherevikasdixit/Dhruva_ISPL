from typing import Optional

from pydantic import BaseModel

from ..common import (
    _ULCATaskType,
    _ULCATextPairMultisuggestion,
    _ULCATransliterationInferenceConfig,
)


class ULCATransliterationInferenceResponse(BaseModel):
    taskType: _ULCATaskType = _ULCATaskType.TRANSLITERATION
    output: list[_ULCATextPairMultisuggestion]
    config: Optional[_ULCATransliterationInferenceConfig]
