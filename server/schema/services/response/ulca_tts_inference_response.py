from typing import Optional

from pydantic import BaseModel

from ..common import _ULCAAudio, _ULCABaseAudioConfig, _ULCATaskType


class ULCATtsInferenceResponse(BaseModel):
    taskType: _ULCATaskType = _ULCATaskType.TTS
    audio: list[_ULCAAudio]
    config: Optional[_ULCABaseAudioConfig]
