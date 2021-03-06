# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/logs/purify_pokemon_log_entry.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2
from pogoprotos.data import pokemon_display_pb2 as pogoprotos_dot_data_dot_pokemon__display__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/logs/purify_pokemon_log_entry.proto',
  package='pogoprotos.data.logs',
  syntax='proto3',
  serialized_pb=_b('\n3pogoprotos/data/logs/purify_pokemon_log_entry.proto\x12\x14pogoprotos.data.logs\x1a!pogoprotos/enums/pokemon_id.proto\x1a%pogoprotos/data/pokemon_display.proto\"\xa1\x01\n\x15PurifyPokemonLogEntry\x12/\n\npokemon_id\x18\x01 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x38\n\x0fpokemon_display\x18\x02 \x01(\x0b\x32\x1f.pogoprotos.data.PokemonDisplay\x12\x1d\n\x15purified_pokemon_uuid\x18\x03 \x01(\x06\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_pokemon__display__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PURIFYPOKEMONLOGENTRY = _descriptor.Descriptor(
  name='PurifyPokemonLogEntry',
  full_name='pogoprotos.data.logs.PurifyPokemonLogEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.data.logs.PurifyPokemonLogEntry.pokemon_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_display', full_name='pogoprotos.data.logs.PurifyPokemonLogEntry.pokemon_display', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='purified_pokemon_uuid', full_name='pogoprotos.data.logs.PurifyPokemonLogEntry.purified_pokemon_uuid', index=2,
      number=3, type=6, cpp_type=4, label=1,
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
  serialized_start=152,
  serialized_end=313,
)

_PURIFYPOKEMONLOGENTRY.fields_by_name['pokemon_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_PURIFYPOKEMONLOGENTRY.fields_by_name['pokemon_display'].message_type = pogoprotos_dot_data_dot_pokemon__display__pb2._POKEMONDISPLAY
DESCRIPTOR.message_types_by_name['PurifyPokemonLogEntry'] = _PURIFYPOKEMONLOGENTRY

PurifyPokemonLogEntry = _reflection.GeneratedProtocolMessageType('PurifyPokemonLogEntry', (_message.Message,), dict(
  DESCRIPTOR = _PURIFYPOKEMONLOGENTRY,
  __module__ = 'pogoprotos.data.logs.purify_pokemon_log_entry_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.logs.PurifyPokemonLogEntry)
  ))
_sym_db.RegisterMessage(PurifyPokemonLogEntry)


# @@protoc_insertion_point(module_scope)
