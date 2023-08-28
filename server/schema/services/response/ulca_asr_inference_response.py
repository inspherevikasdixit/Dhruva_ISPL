from typing import Optional

from pydantic import BaseModel

from ..common import _ULCABaseAudioConfig, _ULCATaskType, _ULCAText

class ULCAAsrInferenceResponseConfig(_ULCABaseAudioConfig):
    postProcessors: Optional[list[str]]

class ULCAAsrInferenceResponse(BaseModel):
    taskType: _ULCATaskType = _ULCATaskType.ASR
    output: list[_ULCAText]
    config: Optional[ULCAAsrInferenceResponseConfig]
