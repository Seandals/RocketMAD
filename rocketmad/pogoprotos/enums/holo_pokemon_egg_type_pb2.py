# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/holo_pokemon_egg_type.proto

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
  name='pogoprotos/enums/holo_pokemon_egg_type.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_pb=_b('\n,pogoprotos/enums/holo_pokemon_egg_type.proto\x12\x10pogoprotos.enums*=\n\x12HoloPokemonEggType\x12\x12\n\x0e\x45GG_TYPE_UNSET\x10\x00\x12\x13\n\x0f\x45GG_TYPE_SHADOW\x10\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_HOLOPOKEMONEGGTYPE = _descriptor.EnumDescriptor(
  name='HoloPokemonEggType',
  full_name='pogoprotos.enums.HoloPokemonEggType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EGG_TYPE_UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EGG_TYPE_SHADOW', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=66,
  serialized_end=127,
)
_sym_db.RegisterEnumDescriptor(_HOLOPOKEMONEGGTYPE)

HoloPokemonEggType = enum_type_wrapper.EnumTypeWrapper(_HOLOPOKEMONEGGTYPE)
EGG_TYPE_UNSET = 0
EGG_TYPE_SHADOW = 1


DESCRIPTOR.enum_types_by_name['HoloPokemonEggType'] = _HOLOPOKEMONEGGTYPE


# @@protoc_insertion_point(module_scope)
