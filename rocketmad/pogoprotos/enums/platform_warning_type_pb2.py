# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/platform_warning_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/platform_warning_type.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n,pogoprotos/enums/platform_warning_type.proto\x12\x10pogoprotos.enums*\x8b\x01\n\x13PlatformWarningType\x12\x1a\n\x16PLATFORM_WARNING_UNSET\x10\x00\x12\x1c\n\x18PLATFORM_WARNING_STRIKE1\x10\x01\x12\x1c\n\x18PLATFORM_WARNING_STRIKE2\x10\x02\x12\x1c\n\x18PLATFORM_WARNING_STRIKE3\x10\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_PLATFORMWARNINGTYPE = _descriptor.EnumDescriptor(
  name='PlatformWarningType',
  full_name='pogoprotos.enums.PlatformWarningType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_WARNING_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_WARNING_STRIKE1', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_WARNING_STRIKE2', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_WARNING_STRIKE3', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=67,
  serialized_end=206,
)
_sym_db.RegisterEnumDescriptor(_PLATFORMWARNINGTYPE)

PlatformWarningType = enum_type_wrapper.EnumTypeWrapper(_PLATFORMWARNINGTYPE)
PLATFORM_WARNING_UNSET = 0
PLATFORM_WARNING_STRIKE1 = 1
PLATFORM_WARNING_STRIKE2 = 2
PLATFORM_WARNING_STRIKE3 = 3


DESCRIPTOR.enum_types_by_name['PlatformWarningType'] = _PLATFORMWARNINGTYPE


# @@protoc_insertion_point(module_scope)
