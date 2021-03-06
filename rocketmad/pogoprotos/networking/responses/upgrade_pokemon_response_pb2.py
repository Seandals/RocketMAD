# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/upgrade_pokemon_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/upgrade_pokemon_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n>pogoprotos/networking/responses/upgrade_pokemon_response.proto\x12\x1fpogoprotos.networking.responses\x1a\"pogoprotos/data/pokemon_data.proto\"\xd5\x05\n\x16UpgradePokemonResponse\x12N\n\x06result\x18\x01 \x01(\x0e\x32>.pogoprotos.networking.responses.UpgradePokemonResponse.Result\x12\x36\n\x10upgraded_pokemon\x18\x02 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12;\n\x15next_upgraded_pokemon\x18\x03 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12j\n\x18\x62ulk_upgrades_cost_table\x18\x04 \x03(\x0b\x32H.pogoprotos.networking.responses.UpgradePokemonResponse.BulkUpgradesCost\x1a\xca\x01\n\x10\x42ulkUpgradesCost\x12\x1a\n\x12number_of_upgrades\x18\x01 \x01(\x05\x12\x15\n\rpokemon_level\x18\x02 \x01(\x05\x12\x12\n\npokemon_cp\x18\x03 \x01(\x05\x12\x1b\n\x13total_stardust_cost\x18\x04 \x01(\x05\x12\x18\n\x10total_candy_cost\x18\x05 \x01(\x05\x12\x1b\n\x13total_cp_multiplier\x18\x06 \x01(\x02\x12\x1b\n\x13total_xl_candy_cost\x18\x07 \x01(\x05\"\xbc\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1b\n\x17\x45RROR_POKEMON_NOT_FOUND\x10\x02\x12 \n\x1c\x45RROR_INSUFFICIENT_RESOURCES\x10\x03\x12\x1f\n\x1b\x45RROR_UPGRADE_NOT_AVAILABLE\x10\x04\x12\x1d\n\x19\x45RROR_POKEMON_IS_DEPLOYED\x10\x05\x12\x1b\n\x17\x45RROR_DUPLICATE_REQUEST\x10\x06\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_UPGRADEPOKEMONRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.UpgradePokemonResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_NOT_FOUND', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INSUFFICIENT_RESOURCES', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_UPGRADE_NOT_AVAILABLE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_IS_DEPLOYED', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_DUPLICATE_REQUEST', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=673,
  serialized_end=861,
)
_sym_db.RegisterEnumDescriptor(_UPGRADEPOKEMONRESPONSE_RESULT)


_UPGRADEPOKEMONRESPONSE_BULKUPGRADESCOST = _descriptor.Descriptor(
  name='BulkUpgradesCost',
  full_name='pogoprotos.networking.responses.UpgradePokemonResponse.BulkUpgradesCost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number_of_upgrades', full_name='pogoprotos.networking.responses.UpgradePokemonResponse.BulkUpgradesCost.number_of_upgrades', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_level', full_name='pogoprotos.networking.responses.UpgradePokemonResponse.BulkUpgradesCost.pokemon_level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_cp', full_name='pogoprotos.networking.responses.UpgradePokemonResponse.BulkUpgradesCost.pokemon_cp', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_stardust_cost', full_name='pogoprotos.networking.responses.UpgradePokemonResponse.BulkUpgradesCost.total_stardust_cost', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_candy_cost', full_name='pogoprotos.networking.responses.UpgradePokemonResponse.BulkUpgradesCost.total_candy_cost', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_cp_multiplier', full_name='pogoprotos.networking.responses.UpgradePokemonResponse.BulkUpgradesCost.total_cp_multiplier', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_xl_candy_cost', full_name='pogoprotos.networking.responses.UpgradePokemonResponse.BulkUpgradesCost.total_xl_candy_cost', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=468,
  serialized_end=670,
)

_UPGRADEPOKEMONRESPONSE = _descriptor.Descriptor(
  name='UpgradePokemonResponse',
  full_name='pogoprotos.networking.responses.UpgradePokemonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.UpgradePokemonResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upgraded_pokemon', full_name='pogoprotos.networking.responses.UpgradePokemonResponse.upgraded_pokemon', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_upgraded_pokemon', full_name='pogoprotos.networking.responses.UpgradePokemonResponse.next_upgraded_pokemon', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bulk_upgrades_cost_table', full_name='pogoprotos.networking.responses.UpgradePokemonResponse.bulk_upgrades_cost_table', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_UPGRADEPOKEMONRESPONSE_BULKUPGRADESCOST, ],
  enum_types=[
    _UPGRADEPOKEMONRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=861,
)

_UPGRADEPOKEMONRESPONSE_BULKUPGRADESCOST.containing_type = _UPGRADEPOKEMONRESPONSE
_UPGRADEPOKEMONRESPONSE.fields_by_name['result'].enum_type = _UPGRADEPOKEMONRESPONSE_RESULT
_UPGRADEPOKEMONRESPONSE.fields_by_name['upgraded_pokemon'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_UPGRADEPOKEMONRESPONSE.fields_by_name['next_upgraded_pokemon'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_UPGRADEPOKEMONRESPONSE.fields_by_name['bulk_upgrades_cost_table'].message_type = _UPGRADEPOKEMONRESPONSE_BULKUPGRADESCOST
_UPGRADEPOKEMONRESPONSE_RESULT.containing_type = _UPGRADEPOKEMONRESPONSE
DESCRIPTOR.message_types_by_name['UpgradePokemonResponse'] = _UPGRADEPOKEMONRESPONSE

UpgradePokemonResponse = _reflection.GeneratedProtocolMessageType('UpgradePokemonResponse', (_message.Message,), dict(

  BulkUpgradesCost = _reflection.GeneratedProtocolMessageType('BulkUpgradesCost', (_message.Message,), dict(
    DESCRIPTOR = _UPGRADEPOKEMONRESPONSE_BULKUPGRADESCOST,
    __module__ = 'pogoprotos.networking.responses.upgrade_pokemon_response_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.UpgradePokemonResponse.BulkUpgradesCost)
    ))
  ,
  DESCRIPTOR = _UPGRADEPOKEMONRESPONSE,
  __module__ = 'pogoprotos.networking.responses.upgrade_pokemon_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.UpgradePokemonResponse)
  ))
_sym_db.RegisterMessage(UpgradePokemonResponse)
_sym_db.RegisterMessage(UpgradePokemonResponse.BulkUpgradesCost)


# @@protoc_insertion_point(module_scope)
