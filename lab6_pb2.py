# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lab6.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nlab6.proto\x12\nrouteguide\"\x1e\n\x06\x61\x64\x64Msg\x12\t\n\x01\x61\x18\x01 \x01(\x05\x12\t\n\x01\x62\x18\x02 \x01(\x05\"\x1a\n\x0brawImageMsg\x12\x0b\n\x03img\x18\x01 \x01(\x0c\"%\n\rdotProductMsg\x12\t\n\x01\x61\x18\x01 \x03(\x02\x12\t\n\x01\x62\x18\x02 \x03(\x02\"\x1b\n\x0cjsonImageMsg\x12\x0b\n\x03img\x18\x01 \x01(\t\"\x17\n\x08\x61\x64\x64Reply\x12\x0b\n\x03sum\x18\x01 \x01(\x05\"%\n\x0f\x64otProductReply\x12\x12\n\ndotproduct\x18\x01 \x01(\x02\"+\n\nimageReply\x12\r\n\x05width\x18\x01 \x01(\x05\x12\x0e\n\x06height\x18\x02 \x01(\x05\x32\x81\x02\n\x04lab6\x12\x31\n\x03\x61\x64\x64\x12\x12.routeguide.addMsg\x1a\x14.routeguide.addReply\"\x00\x12=\n\x08rawImage\x12\x17.routeguide.rawImageMsg\x1a\x16.routeguide.imageReply\"\x00\x12\x46\n\ndotProduct\x12\x19.routeguide.dotProductMsg\x1a\x1b.routeguide.dotProductReply\"\x00\x12?\n\tjsonImage\x12\x18.routeguide.jsonImageMsg\x1a\x16.routeguide.imageReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'lab6_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ADDMSG._serialized_start=26
  _ADDMSG._serialized_end=56
  _RAWIMAGEMSG._serialized_start=58
  _RAWIMAGEMSG._serialized_end=84
  _DOTPRODUCTMSG._serialized_start=86
  _DOTPRODUCTMSG._serialized_end=123
  _JSONIMAGEMSG._serialized_start=125
  _JSONIMAGEMSG._serialized_end=152
  _ADDREPLY._serialized_start=154
  _ADDREPLY._serialized_end=177
  _DOTPRODUCTREPLY._serialized_start=179
  _DOTPRODUCTREPLY._serialized_end=216
  _IMAGEREPLY._serialized_start=218
  _IMAGEREPLY._serialized_end=261
  _LAB6._serialized_start=264
  _LAB6._serialized_end=521
# @@protoc_insertion_point(module_scope)