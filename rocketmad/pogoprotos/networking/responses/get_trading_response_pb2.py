# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_trading_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.trading import trading_pb2 as pogoprotos_dot_data_dot_trading_dot_trading__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_trading_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n:pogoprotos/networking/responses/get_trading_response.proto\x12\x1fpogoprotos.networking.responses\x1a%pogoprotos/data/trading/trading.proto\"\xb4\x02\n\x12GetTradingResponse\x12J\n\x06result\x18\x01 \x01(\x0e\x32:.pogoprotos.networking.responses.GetTradingResponse.Result\x12\x31\n\x07trading\x18\x02 \x01(\x0b\x32 .pogoprotos.data.trading.Trading\"\x9e\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x11\n\rERROR_UNKNOWN\x10\x02\x12\x1a\n\x16\x45RROR_FRIEND_NOT_FOUND\x10\x03\x12\x1b\n\x17\x45RROR_INVALID_PLAYER_ID\x10\x04\x12\x17\n\x13\x45RROR_INVALID_STATE\x10\x05\x12\x17\n\x13\x45RROR_STATE_HANDLER\x10\x06\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_trading_dot_trading__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETTRADINGRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.GetTradingResponse.Result',
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
      name='ERROR_UNKNOWN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_FRIEND_NOT_FOUND', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_PLAYER_ID', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_STATE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_STATE_HANDLER', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=285,
  serialized_end=443,
)
_sym_db.RegisterEnumDescriptor(_GETTRADINGRESPONSE_RESULT)


_GETTRADINGRESPONSE = _descriptor.Descriptor(
  name='GetTradingResponse',
  full_name='pogoprotos.networking.responses.GetTradingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.GetTradingResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trading', full_name='pogoprotos.networking.responses.GetTradingResponse.trading', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETTRADINGRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=443,
)

_GETTRADINGRESPONSE.fields_by_name['result'].enum_type = _GETTRADINGRESPONSE_RESULT
_GETTRADINGRESPONSE.fields_by_name['trading'].message_type = pogoprotos_dot_data_dot_trading_dot_trading__pb2._TRADING
_GETTRADINGRESPONSE_RESULT.containing_type = _GETTRADINGRESPONSE
DESCRIPTOR.message_types_by_name['GetTradingResponse'] = _GETTRADINGRESPONSE

GetTradingResponse = _reflection.GeneratedProtocolMessageType('GetTradingResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETTRADINGRESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_trading_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetTradingResponse)
  ))
_sym_db.RegisterMessage(GetTradingResponse)


# @@protoc_insertion_point(module_scope)