# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/vs_seeker_reward_encounter_response.proto

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
from pogoprotos.data.capture import capture_probability_pb2 as pogoprotos_dot_data_dot_capture_dot_capture__probability__pb2
from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/vs_seeker_reward_encounter_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\nIpogoprotos/networking/responses/vs_seeker_reward_encounter_response.proto\x12\x1fpogoprotos.networking.responses\x1a\"pogoprotos/data/pokemon_data.proto\x1a\x31pogoprotos/data/capture/capture_probability.proto\x1a\'pogoprotos/inventory/item/item_id.proto\"\x98\x04\n\x1fVsSeekerRewardEncounterResponse\x12W\n\x06result\x18\x01 \x01(\x0e\x32G.pogoprotos.networking.responses.VsSeekerRewardEncounterResponse.Result\x12-\n\x07pokemon\x18\x02 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12H\n\x13\x63\x61pture_probability\x18\x03 \x01(\x0b\x32+.pogoprotos.data.capture.CaptureProbability\x12\x36\n\x0b\x61\x63tive_item\x18\x04 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemId\x12\x14\n\x0c\x65ncounter_id\x18\x05 \x01(\x06\"\xd4\x01\n\x06Result\x12\x1f\n\x1bVS_SEEKER_ENCOUNTER_UNKNOWN\x10\x00\x12\x1f\n\x1bVS_SEEKER_ENCOUNTER_SUCCESS\x10\x01\x12(\n$VS_SEEKER_ENCOUNTER_ALREADY_FINISHED\x10\x02\x12%\n!ERROR_PLAYER_NOT_ENOUGH_VICTORIES\x10\x03\x12 \n\x1c\x45RROR_POKEMON_INVENTORY_FULL\x10\x04\x12\x15\n\x11\x45RROR_REDEEM_ITEM\x10\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_capture_dot_capture__probability__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_VSSEEKERREWARDENCOUNTERRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.VsSeekerRewardEncounterResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VS_SEEKER_ENCOUNTER_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VS_SEEKER_ENCOUNTER_SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VS_SEEKER_ENCOUNTER_ALREADY_FINISHED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_PLAYER_NOT_ENOUGH_VICTORIES', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_INVENTORY_FULL', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_REDEEM_ITEM', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=563,
  serialized_end=775,
)
_sym_db.RegisterEnumDescriptor(_VSSEEKERREWARDENCOUNTERRESPONSE_RESULT)


_VSSEEKERREWARDENCOUNTERRESPONSE = _descriptor.Descriptor(
  name='VsSeekerRewardEncounterResponse',
  full_name='pogoprotos.networking.responses.VsSeekerRewardEncounterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.VsSeekerRewardEncounterResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon', full_name='pogoprotos.networking.responses.VsSeekerRewardEncounterResponse.pokemon', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='capture_probability', full_name='pogoprotos.networking.responses.VsSeekerRewardEncounterResponse.capture_probability', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='active_item', full_name='pogoprotos.networking.responses.VsSeekerRewardEncounterResponse.active_item', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encounter_id', full_name='pogoprotos.networking.responses.VsSeekerRewardEncounterResponse.encounter_id', index=4,
      number=5, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VSSEEKERREWARDENCOUNTERRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=239,
  serialized_end=775,
)

_VSSEEKERREWARDENCOUNTERRESPONSE.fields_by_name['result'].enum_type = _VSSEEKERREWARDENCOUNTERRESPONSE_RESULT
_VSSEEKERREWARDENCOUNTERRESPONSE.fields_by_name['pokemon'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_VSSEEKERREWARDENCOUNTERRESPONSE.fields_by_name['capture_probability'].message_type = pogoprotos_dot_data_dot_capture_dot_capture__probability__pb2._CAPTUREPROBABILITY
_VSSEEKERREWARDENCOUNTERRESPONSE.fields_by_name['active_item'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
_VSSEEKERREWARDENCOUNTERRESPONSE_RESULT.containing_type = _VSSEEKERREWARDENCOUNTERRESPONSE
DESCRIPTOR.message_types_by_name['VsSeekerRewardEncounterResponse'] = _VSSEEKERREWARDENCOUNTERRESPONSE

VsSeekerRewardEncounterResponse = _reflection.GeneratedProtocolMessageType('VsSeekerRewardEncounterResponse', (_message.Message,), dict(
  DESCRIPTOR = _VSSEEKERREWARDENCOUNTERRESPONSE,
  __module__ = 'pogoprotos.networking.responses.vs_seeker_reward_encounter_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.VsSeekerRewardEncounterResponse)
  ))
_sym_db.RegisterMessage(VsSeekerRewardEncounterResponse)


# @@protoc_insertion_point(module_scope)
