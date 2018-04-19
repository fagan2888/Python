# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: security/DeviceToken.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from device import Device_pb2 as device_dot_Device__pb2
from security import Token_pb2 as security_dot_Token__pb2
from temporal import Instant_pb2 as temporal_dot_Instant__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='security/DeviceToken.proto',
  package='bloombox.schema.security',
  syntax='proto3',
  serialized_pb=_b('\n\x1asecurity/DeviceToken.proto\x12\x18\x62loombox.schema.security\x1a\x13\x64\x65vice/Device.proto\x1a\x14security/Token.proto\x1a\x16temporal/Instant.proto\"\xcf\x01\n\x0b\x44\x65viceToken\x12\x32\n\x05token\x18\x01 \x01(\x0b\x32#.bloombox.schema.security.AuthToken\x12+\n\x06\x64\x65vice\x18\x02 \x01(\x0b\x32\x1b.opencannabis.device.Device\x12.\n\x06issued\x18\x03 \x01(\x0b\x32\x1e.opencannabis.temporal.Instant\x12/\n\x07\x65xpires\x18\x04 \x01(\x0b\x32\x1e.opencannabis.temporal.InstantB\'\n\x1bio.bloombox.schema.securityH\x01P\x01\xa2\x02\x03\x42\x42Sb\x06proto3')
  ,
  dependencies=[device_dot_Device__pb2.DESCRIPTOR,security_dot_Token__pb2.DESCRIPTOR,temporal_dot_Instant__pb2.DESCRIPTOR,])




_DEVICETOKEN = _descriptor.Descriptor(
  name='DeviceToken',
  full_name='bloombox.schema.security.DeviceToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='bloombox.schema.security.DeviceToken.token', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='bloombox.schema.security.DeviceToken.device', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issued', full_name='bloombox.schema.security.DeviceToken.issued', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expires', full_name='bloombox.schema.security.DeviceToken.expires', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=124,
  serialized_end=331,
)

_DEVICETOKEN.fields_by_name['token'].message_type = security_dot_Token__pb2._AUTHTOKEN
_DEVICETOKEN.fields_by_name['device'].message_type = device_dot_Device__pb2._DEVICE
_DEVICETOKEN.fields_by_name['issued'].message_type = temporal_dot_Instant__pb2._INSTANT
_DEVICETOKEN.fields_by_name['expires'].message_type = temporal_dot_Instant__pb2._INSTANT
DESCRIPTOR.message_types_by_name['DeviceToken'] = _DEVICETOKEN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceToken = _reflection.GeneratedProtocolMessageType('DeviceToken', (_message.Message,), dict(
  DESCRIPTOR = _DEVICETOKEN,
  __module__ = 'security.DeviceToken_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.security.DeviceToken)
  ))
_sym_db.RegisterMessage(DeviceToken)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.bloombox.schema.securityH\001P\001\242\002\003BBS'))
# @@protoc_insertion_point(module_scope)
