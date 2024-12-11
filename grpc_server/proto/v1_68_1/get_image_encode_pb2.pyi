from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DlEmbeddingRequest(_message.Message):
    __slots__ = ("imdata", "imsize")
    IMDATA_FIELD_NUMBER: _ClassVar[int]
    IMSIZE_FIELD_NUMBER: _ClassVar[int]
    imdata: bytes
    imsize: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, imdata: _Optional[bytes] = ..., imsize: _Optional[_Iterable[int]] = ...) -> None: ...

class Tensor(_message.Message):
    __slots__ = ("data", "shape")
    DATA_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedScalarFieldContainer[float]
    shape: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, data: _Optional[_Iterable[float]] = ..., shape: _Optional[_Iterable[int]] = ...) -> None: ...
