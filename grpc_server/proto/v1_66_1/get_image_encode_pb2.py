# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: get_image_encode.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'get_image_encode.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16get_image_encode.proto\x12\taiservice\"4\n\x12\x44lEmbeddingRequest\x12\x0e\n\x06imdata\x18\x01 \x01(\x0c\x12\x0e\n\x06imsize\x18\x02 \x03(\x05\"%\n\x06Tensor\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x02\x12\r\n\x05shape\x18\x02 \x03(\x05\x32Q\n\tAiService\x12\x44\n\x0e\x44lEmbeddingGet\x12\x1d.aiservice.DlEmbeddingRequest\x1a\x11.aiservice.Tensor\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'get_image_encode_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DLEMBEDDINGREQUEST']._serialized_start=37
  _globals['_DLEMBEDDINGREQUEST']._serialized_end=89
  _globals['_TENSOR']._serialized_start=91
  _globals['_TENSOR']._serialized_end=128
  _globals['_AISERVICE']._serialized_start=130
  _globals['_AISERVICE']._serialized_end=211
# @@protoc_insertion_point(module_scope)