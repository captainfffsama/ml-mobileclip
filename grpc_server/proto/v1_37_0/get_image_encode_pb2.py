# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_image_encode.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_image_encode.proto',
  package='aiservice',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16get_image_encode.proto\x12\taiservice\"4\n\x12\x44lEmbeddingRequest\x12\x0e\n\x06imdata\x18\x01 \x01(\x0c\x12\x0e\n\x06imsize\x18\x02 \x03(\x05\"%\n\x06Tensor\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x02\x12\r\n\x05shape\x18\x02 \x03(\x05\x32Q\n\tAiService\x12\x44\n\x0e\x44lEmbeddingGet\x12\x1d.aiservice.DlEmbeddingRequest\x1a\x11.aiservice.Tensor\"\x00\x62\x06proto3'
)




_DLEMBEDDINGREQUEST = _descriptor.Descriptor(
  name='DlEmbeddingRequest',
  full_name='aiservice.DlEmbeddingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='imdata', full_name='aiservice.DlEmbeddingRequest.imdata', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imsize', full_name='aiservice.DlEmbeddingRequest.imsize', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=89,
)


_TENSOR = _descriptor.Descriptor(
  name='Tensor',
  full_name='aiservice.Tensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='aiservice.Tensor.data', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shape', full_name='aiservice.Tensor.shape', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=128,
)

DESCRIPTOR.message_types_by_name['DlEmbeddingRequest'] = _DLEMBEDDINGREQUEST
DESCRIPTOR.message_types_by_name['Tensor'] = _TENSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DlEmbeddingRequest = _reflection.GeneratedProtocolMessageType('DlEmbeddingRequest', (_message.Message,), {
  'DESCRIPTOR' : _DLEMBEDDINGREQUEST,
  '__module__' : 'get_image_encode_pb2'
  # @@protoc_insertion_point(class_scope:aiservice.DlEmbeddingRequest)
  })
_sym_db.RegisterMessage(DlEmbeddingRequest)

Tensor = _reflection.GeneratedProtocolMessageType('Tensor', (_message.Message,), {
  'DESCRIPTOR' : _TENSOR,
  '__module__' : 'get_image_encode_pb2'
  # @@protoc_insertion_point(class_scope:aiservice.Tensor)
  })
_sym_db.RegisterMessage(Tensor)



_AISERVICE = _descriptor.ServiceDescriptor(
  name='AiService',
  full_name='aiservice.AiService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=130,
  serialized_end=211,
  methods=[
  _descriptor.MethodDescriptor(
    name='DlEmbeddingGet',
    full_name='aiservice.AiService.DlEmbeddingGet',
    index=0,
    containing_service=None,
    input_type=_DLEMBEDDINGREQUEST,
    output_type=_TENSOR,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AISERVICE)

DESCRIPTOR.services_by_name['AiService'] = _AISERVICE

# @@protoc_insertion_point(module_scope)