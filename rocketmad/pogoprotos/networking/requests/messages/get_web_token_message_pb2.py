# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/get_web_token_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/get_web_token_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nCpogoprotos/networking/requests/messages/get_web_token_message.proto\x12\'pogoprotos.networking.requests.messages\"\'\n\x12GetWebTokenMessage\x12\x11\n\tclient_id\x18\x01 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETWEBTOKENMESSAGE = _descriptor.Descriptor(
  name='GetWebTokenMessage',
  full_name='pogoprotos.networking.requests.messages.GetWebTokenMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='pogoprotos.networking.requests.messages.GetWebTokenMessage.client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=112,
  serialized_end=151,
)

DESCRIPTOR.message_types_by_name['GetWebTokenMessage'] = _GETWEBTOKENMESSAGE

GetWebTokenMessage = _reflection.GeneratedProtocolMessageType('GetWebTokenMessage', (_message.Message,), dict(
  DESCRIPTOR = _GETWEBTOKENMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.get_web_token_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.GetWebTokenMessage)
  ))
_sym_db.RegisterMessage(GetWebTokenMessage)


# @@protoc_insertion_point(module_scope)
