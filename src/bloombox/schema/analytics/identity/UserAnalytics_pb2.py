# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analytics/identity/UserAnalytics.proto

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


from temporal import Instant_pb2 as temporal_dot_Instant__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='analytics/identity/UserAnalytics.proto',
  package='bloombox.schema.analytics.identity',
  syntax='proto3',
  serialized_pb=_b('\n&analytics/identity/UserAnalytics.proto\x12\"bloombox.schema.analytics.identity\x1a\x16temporal/Instant.proto\"\x8a\x01\n\x06\x41\x63tion\x12\x10\n\x08identity\x18\x01 \x01(\t\x12<\n\x04verb\x18\x02 \x01(\x0e\x32..bloombox.schema.analytics.identity.UserAction\x12\x30\n\x08occurred\x18\x03 \x01(\x0b\x32\x1e.opencannabis.temporal.Instant*\x98\x01\n\nUserAction\x12\n\n\x06\x45NGAGE\x10\x00\x12\n\n\x06\x45NROLL\x10\n\x12\x0c\n\x08\x41\x43TIVATE\x10\x0b\x12\x08\n\x04JOIN\x10\x0c\x12\n\n\x06VERIFY\x10\r\x12\x0b\n\x07\x43HECKIN\x10\x0e\x12\x0f\n\x0bPREFERENCES\x10\x0f\x12\x0c\n\x08PURCHASE\x10\x10\x12\t\n\x05ORDER\x10\x11\x12\n\n\x06OPT_IN\x10\x12\x12\x0b\n\x07OPT_OUT\x10\x13\x42<\n!io.bloombox.schema.analytics.userB\rUserAnalyticsH\x01P\x00\xa2\x02\x03\x42\x42Sb\x06proto3')
  ,
  dependencies=[temporal_dot_Instant__pb2.DESCRIPTOR,])

_USERACTION = _descriptor.EnumDescriptor(
  name='UserAction',
  full_name='bloombox.schema.analytics.identity.UserAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENGAGE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENROLL', index=1, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVATE', index=2, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOIN', index=3, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERIFY', index=4, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECKIN', index=5, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREFERENCES', index=6, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PURCHASE', index=7, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDER', index=8, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPT_IN', index=9, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPT_OUT', index=10, number=19,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=244,
  serialized_end=396,
)
_sym_db.RegisterEnumDescriptor(_USERACTION)

UserAction = enum_type_wrapper.EnumTypeWrapper(_USERACTION)
ENGAGE = 0
ENROLL = 10
ACTIVATE = 11
JOIN = 12
VERIFY = 13
CHECKIN = 14
PREFERENCES = 15
PURCHASE = 16
ORDER = 17
OPT_IN = 18
OPT_OUT = 19



_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='bloombox.schema.analytics.identity.Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identity', full_name='bloombox.schema.analytics.identity.Action.identity', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='verb', full_name='bloombox.schema.analytics.identity.Action.verb', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occurred', full_name='bloombox.schema.analytics.identity.Action.occurred', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=103,
  serialized_end=241,
)

_ACTION.fields_by_name['verb'].enum_type = _USERACTION
_ACTION.fields_by_name['occurred'].message_type = temporal_dot_Instant__pb2._INSTANT
DESCRIPTOR.message_types_by_name['Action'] = _ACTION
DESCRIPTOR.enum_types_by_name['UserAction'] = _USERACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), dict(
  DESCRIPTOR = _ACTION,
  __module__ = 'analytics.identity.UserAnalytics_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.analytics.identity.Action)
  ))
_sym_db.RegisterMessage(Action)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!io.bloombox.schema.analytics.userB\rUserAnalyticsH\001P\000\242\002\003BBS'))
# @@protoc_insertion_point(module_scope)
