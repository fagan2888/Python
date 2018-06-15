# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: checkin/v1beta1/CheckinService_Beta1.proto

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


from identity import User_pb2 as identity_dot_User__pb2
from identity import UserKey_pb2 as identity_dot_UserKey__pb2
from services import ServiceStatus_pb2 as services_dot_ServiceStatus__pb2
from person import PersonName_pb2 as person_dot_PersonName__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='checkin/v1beta1/CheckinService_Beta1.proto',
  package='bloombox.schema.services.checkin.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n*checkin/v1beta1/CheckinService_Beta1.proto\x12(bloombox.schema.services.checkin.v1beta1\x1a\x13identity/User.proto\x1a\x16identity/UserKey.proto\x1a\x1cservices/ServiceStatus.proto\x1a\x17person/PersonName.proto\x1a\x1cgoogle/api/annotations.proto\"\xf8\x01\n\x04Ping\x1a\t\n\x07Request\x1a\x43\n\x08Response\x12\x37\n\x06status\x18\x01 \x01(\x0e\x32\'.bloombox.schema.services.ServiceStatus\x1a\x9f\x01\n\tOperation\x12G\n\x07request\x18\x01 \x01(\x0b\x32\x36.bloombox.schema.services.checkin.v1beta1.Ping.Request\x12I\n\x08response\x18\x02 \x01(\x0b\x32\x37.bloombox.schema.services.checkin.v1beta1.Ping.Response\"\x9a\x01\n\x0b\x43heckinUser\x12.\n\x03key\x18\x01 \x01(\x0b\x32!.bloombox.schema.identity.UserKey\x12\x32\n\x05\x66lags\x18\x02 \x01(\x0b\x32#.bloombox.schema.identity.UserFlags\x12\'\n\x04name\x18\x03 \x01(\x0b\x32\x19.opencannabis.person.Name\"!\n\x11\x43heckinEnrollment\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\"\x94\x02\n\x0f\x43heckinResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x13\n\x0bmust_enroll\x18\x02 \x01(\x08\x12\x45\n\x05\x65rror\x18\x03 \x01(\x0e\x32\x36.bloombox.schema.services.checkin.v1beta1.CheckinError\x12\x43\n\x04user\x18\x04 \x01(\x0b\x32\x35.bloombox.schema.services.checkin.v1beta1.CheckinUser\x12O\n\nenrollment\x18\x05 \x01(\x0b\x32;.bloombox.schema.services.checkin.v1beta1.CheckinEnrollment\"\x87\x02\n\tIDCheckin\x1aQ\n\x07Request\x12\x0b\n\x03raw\x18\x01 \x01(\t\x12\r\n\x05scope\x18\x02 \x01(\t\x12\x15\n\rserial_number\x18\x03 \x01(\t\x12\x13\n\x0b\x66ingerprint\x18\x04 \x01(\t\x1a\xa6\x01\n\tOperation\x12L\n\x07request\x18\x01 \x01(\x0b\x32;.bloombox.schema.services.checkin.v1beta1.IDCheckin.Request\x12K\n\x08response\x18\x02 \x01(\x0b\x32\x39.bloombox.schema.services.checkin.v1beta1.CheckinResponse\"\x98\x02\n\x0b\x43\x61rdCheckin\x1a^\n\x07Request\x12\x11\n\tcard_type\x18\x01 \x01(\t\x12\x0f\n\x07payload\x18\x02 \x01(\t\x12\x11\n\tsignature\x18\x03 \x01(\t\x12\r\n\x05\x61gent\x18\x04 \x01(\t\x12\r\n\x05scope\x18\x05 \x01(\t\x1a\xa8\x01\n\tOperation\x12N\n\x07request\x18\x01 \x01(\x0b\x32=.bloombox.schema.services.checkin.v1beta1.CardCheckin.Request\x12K\n\x08response\x18\x02 \x01(\x0b\x32\x39.bloombox.schema.services.checkin.v1beta1.CheckinResponse*\xc5\x02\n\x0c\x43heckinError\x12\x0c\n\x08NO_ERROR\x10\x00\x12\x10\n\x0cID_NOT_FOUND\x10\x01\x12\x0e\n\nID_EXPIRED\x10\x02\x12\x0e\n\nID_INVALID\x10\x03\x12\x17\n\x13ID_TYPE_UNSUPPORTED\x10\x04\x12\x15\n\x11\x43\x41RD_TYPE_INVALID\x10\x05\x12\x10\n\x0c\x43\x41RD_EXPIRED\x10\x06\x12\x12\n\x0e\x43\x41RD_SUSPENDED\x10\x07\x12\x12\n\x0eUSER_SUSPENDED\x10\x08\x12\x15\n\x11PARTNER_SUSPENDED\x10\t\x12\x13\n\x0fPARTNER_INVALID\x10\n\x12\x14\n\x10LOCATION_INVALID\x10\x0b\x12\x18\n\x14JURISDICTION_INVALID\x10\x0c\x12\x1c\n\x18JURISDICTION_UNSUPPORTED\x10\r\x12\x11\n\rUSER_UNDERAGE\x10\x0e\x32\xc0\x04\n\x07\x43heckin\x12\x96\x01\n\x04Ping\x12\x36.bloombox.schema.services.checkin.v1beta1.Ping.Request\x1a\x37.bloombox.schema.services.checkin.v1beta1.Ping.Response\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/checkin/v1beta1/ping\x12\xef\x01\n\x0eIdentification\x12;.bloombox.schema.services.checkin.v1beta1.IDCheckin.Request\x1a\x39.bloombox.schema.services.checkin.v1beta1.CheckinResponse\"e\x82\xd3\xe4\x93\x02_\"9/checkin/v1beta1/{scope=partners/*/locations/*}/global:id:\x01*Z\x1f\"\x1a/checkin/v1beta1/global:id:\x01*\x12\xa9\x01\n\x04\x43\x61rd\x12=.bloombox.schema.services.checkin.v1beta1.CardCheckin.Request\x1a\x39.bloombox.schema.services.checkin.v1beta1.CheckinResponse\"\'\x82\xd3\xe4\x93\x02!\"\x1c/checkin/v1beta1/global:card:\x01*B7\n+io.bloombox.schema.services.checkin.v1beta1H\x01P\x01\xa2\x02\x03\x42\x42Sb\x06proto3')
  ,
  dependencies=[identity_dot_User__pb2.DESCRIPTOR,identity_dot_UserKey__pb2.DESCRIPTOR,services_dot_ServiceStatus__pb2.DESCRIPTOR,person_dot_PersonName__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])

_CHECKINERROR = _descriptor.EnumDescriptor(
  name='CheckinError',
  full_name='bloombox.schema.services.checkin.v1beta1.CheckinError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_ERROR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_NOT_FOUND', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_EXPIRED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_INVALID', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ID_TYPE_UNSUPPORTED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARD_TYPE_INVALID', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARD_EXPIRED', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARD_SUSPENDED', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_SUSPENDED', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARTNER_SUSPENDED', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PARTNER_INVALID', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_INVALID', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JURISDICTION_INVALID', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JURISDICTION_UNSUPPORTED', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USER_UNDERAGE', index=14, number=14,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1490,
  serialized_end=1815,
)
_sym_db.RegisterEnumDescriptor(_CHECKINERROR)

CheckinError = enum_type_wrapper.EnumTypeWrapper(_CHECKINERROR)
NO_ERROR = 0
ID_NOT_FOUND = 1
ID_EXPIRED = 2
ID_INVALID = 3
ID_TYPE_UNSUPPORTED = 4
CARD_TYPE_INVALID = 5
CARD_EXPIRED = 6
CARD_SUSPENDED = 7
USER_SUSPENDED = 8
PARTNER_SUSPENDED = 9
PARTNER_INVALID = 10
LOCATION_INVALID = 11
JURISDICTION_INVALID = 12
JURISDICTION_UNSUPPORTED = 13
USER_UNDERAGE = 14



_PING_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='bloombox.schema.services.checkin.v1beta1.Ping.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=227,
  serialized_end=236,
)

_PING_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='bloombox.schema.services.checkin.v1beta1.Ping.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='bloombox.schema.services.checkin.v1beta1.Ping.Response.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=238,
  serialized_end=305,
)

_PING_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='bloombox.schema.services.checkin.v1beta1.Ping.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='bloombox.schema.services.checkin.v1beta1.Ping.Operation.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='bloombox.schema.services.checkin.v1beta1.Ping.Operation.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=308,
  serialized_end=467,
)

_PING = _descriptor.Descriptor(
  name='Ping',
  full_name='bloombox.schema.services.checkin.v1beta1.Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_PING_REQUEST, _PING_RESPONSE, _PING_OPERATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=467,
)


_CHECKINUSER = _descriptor.Descriptor(
  name='CheckinUser',
  full_name='bloombox.schema.services.checkin.v1beta1.CheckinUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bloombox.schema.services.checkin.v1beta1.CheckinUser.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flags', full_name='bloombox.schema.services.checkin.v1beta1.CheckinUser.flags', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='bloombox.schema.services.checkin.v1beta1.CheckinUser.name', index=2,
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
  serialized_start=470,
  serialized_end=624,
)


_CHECKINENROLLMENT = _descriptor.Descriptor(
  name='CheckinEnrollment',
  full_name='bloombox.schema.services.checkin.v1beta1.CheckinEnrollment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='bloombox.schema.services.checkin.v1beta1.CheckinEnrollment.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=626,
  serialized_end=659,
)


_CHECKINRESPONSE = _descriptor.Descriptor(
  name='CheckinResponse',
  full_name='bloombox.schema.services.checkin.v1beta1.CheckinResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='bloombox.schema.services.checkin.v1beta1.CheckinResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='must_enroll', full_name='bloombox.schema.services.checkin.v1beta1.CheckinResponse.must_enroll', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='bloombox.schema.services.checkin.v1beta1.CheckinResponse.error', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='bloombox.schema.services.checkin.v1beta1.CheckinResponse.user', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enrollment', full_name='bloombox.schema.services.checkin.v1beta1.CheckinResponse.enrollment', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=662,
  serialized_end=938,
)


_IDCHECKIN_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='bloombox.schema.services.checkin.v1beta1.IDCheckin.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raw', full_name='bloombox.schema.services.checkin.v1beta1.IDCheckin.Request.raw', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scope', full_name='bloombox.schema.services.checkin.v1beta1.IDCheckin.Request.scope', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serial_number', full_name='bloombox.schema.services.checkin.v1beta1.IDCheckin.Request.serial_number', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fingerprint', full_name='bloombox.schema.services.checkin.v1beta1.IDCheckin.Request.fingerprint', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=954,
  serialized_end=1035,
)

_IDCHECKIN_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='bloombox.schema.services.checkin.v1beta1.IDCheckin.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='bloombox.schema.services.checkin.v1beta1.IDCheckin.Operation.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='bloombox.schema.services.checkin.v1beta1.IDCheckin.Operation.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=1038,
  serialized_end=1204,
)

_IDCHECKIN = _descriptor.Descriptor(
  name='IDCheckin',
  full_name='bloombox.schema.services.checkin.v1beta1.IDCheckin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_IDCHECKIN_REQUEST, _IDCHECKIN_OPERATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=941,
  serialized_end=1204,
)


_CARDCHECKIN_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='bloombox.schema.services.checkin.v1beta1.CardCheckin.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='card_type', full_name='bloombox.schema.services.checkin.v1beta1.CardCheckin.Request.card_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='bloombox.schema.services.checkin.v1beta1.CardCheckin.Request.payload', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='bloombox.schema.services.checkin.v1beta1.CardCheckin.Request.signature', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agent', full_name='bloombox.schema.services.checkin.v1beta1.CardCheckin.Request.agent', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scope', full_name='bloombox.schema.services.checkin.v1beta1.CardCheckin.Request.scope', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1222,
  serialized_end=1316,
)

_CARDCHECKIN_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='bloombox.schema.services.checkin.v1beta1.CardCheckin.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='bloombox.schema.services.checkin.v1beta1.CardCheckin.Operation.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='response', full_name='bloombox.schema.services.checkin.v1beta1.CardCheckin.Operation.response', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=1319,
  serialized_end=1487,
)

_CARDCHECKIN = _descriptor.Descriptor(
  name='CardCheckin',
  full_name='bloombox.schema.services.checkin.v1beta1.CardCheckin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_CARDCHECKIN_REQUEST, _CARDCHECKIN_OPERATION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1207,
  serialized_end=1487,
)

_PING_REQUEST.containing_type = _PING
_PING_RESPONSE.fields_by_name['status'].enum_type = services_dot_ServiceStatus__pb2._SERVICESTATUS
_PING_RESPONSE.containing_type = _PING
_PING_OPERATION.fields_by_name['request'].message_type = _PING_REQUEST
_PING_OPERATION.fields_by_name['response'].message_type = _PING_RESPONSE
_PING_OPERATION.containing_type = _PING
_CHECKINUSER.fields_by_name['key'].message_type = identity_dot_UserKey__pb2._USERKEY
_CHECKINUSER.fields_by_name['flags'].message_type = identity_dot_User__pb2._USERFLAGS
_CHECKINUSER.fields_by_name['name'].message_type = person_dot_PersonName__pb2._NAME
_CHECKINRESPONSE.fields_by_name['error'].enum_type = _CHECKINERROR
_CHECKINRESPONSE.fields_by_name['user'].message_type = _CHECKINUSER
_CHECKINRESPONSE.fields_by_name['enrollment'].message_type = _CHECKINENROLLMENT
_IDCHECKIN_REQUEST.containing_type = _IDCHECKIN
_IDCHECKIN_OPERATION.fields_by_name['request'].message_type = _IDCHECKIN_REQUEST
_IDCHECKIN_OPERATION.fields_by_name['response'].message_type = _CHECKINRESPONSE
_IDCHECKIN_OPERATION.containing_type = _IDCHECKIN
_CARDCHECKIN_REQUEST.containing_type = _CARDCHECKIN
_CARDCHECKIN_OPERATION.fields_by_name['request'].message_type = _CARDCHECKIN_REQUEST
_CARDCHECKIN_OPERATION.fields_by_name['response'].message_type = _CHECKINRESPONSE
_CARDCHECKIN_OPERATION.containing_type = _CARDCHECKIN
DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.message_types_by_name['CheckinUser'] = _CHECKINUSER
DESCRIPTOR.message_types_by_name['CheckinEnrollment'] = _CHECKINENROLLMENT
DESCRIPTOR.message_types_by_name['CheckinResponse'] = _CHECKINRESPONSE
DESCRIPTOR.message_types_by_name['IDCheckin'] = _IDCHECKIN
DESCRIPTOR.message_types_by_name['CardCheckin'] = _CARDCHECKIN
DESCRIPTOR.enum_types_by_name['CheckinError'] = _CHECKINERROR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), dict(

  Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
    DESCRIPTOR = _PING_REQUEST,
    __module__ = 'checkin.v1beta1.CheckinService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.checkin.v1beta1.Ping.Request)
    ))
  ,

  Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
    DESCRIPTOR = _PING_RESPONSE,
    __module__ = 'checkin.v1beta1.CheckinService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.checkin.v1beta1.Ping.Response)
    ))
  ,

  Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), dict(
    DESCRIPTOR = _PING_OPERATION,
    __module__ = 'checkin.v1beta1.CheckinService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.checkin.v1beta1.Ping.Operation)
    ))
  ,
  DESCRIPTOR = _PING,
  __module__ = 'checkin.v1beta1.CheckinService_Beta1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.checkin.v1beta1.Ping)
  ))
_sym_db.RegisterMessage(Ping)
_sym_db.RegisterMessage(Ping.Request)
_sym_db.RegisterMessage(Ping.Response)
_sym_db.RegisterMessage(Ping.Operation)

CheckinUser = _reflection.GeneratedProtocolMessageType('CheckinUser', (_message.Message,), dict(
  DESCRIPTOR = _CHECKINUSER,
  __module__ = 'checkin.v1beta1.CheckinService_Beta1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.checkin.v1beta1.CheckinUser)
  ))
_sym_db.RegisterMessage(CheckinUser)

CheckinEnrollment = _reflection.GeneratedProtocolMessageType('CheckinEnrollment', (_message.Message,), dict(
  DESCRIPTOR = _CHECKINENROLLMENT,
  __module__ = 'checkin.v1beta1.CheckinService_Beta1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.checkin.v1beta1.CheckinEnrollment)
  ))
_sym_db.RegisterMessage(CheckinEnrollment)

CheckinResponse = _reflection.GeneratedProtocolMessageType('CheckinResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHECKINRESPONSE,
  __module__ = 'checkin.v1beta1.CheckinService_Beta1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.checkin.v1beta1.CheckinResponse)
  ))
_sym_db.RegisterMessage(CheckinResponse)

IDCheckin = _reflection.GeneratedProtocolMessageType('IDCheckin', (_message.Message,), dict(

  Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
    DESCRIPTOR = _IDCHECKIN_REQUEST,
    __module__ = 'checkin.v1beta1.CheckinService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.checkin.v1beta1.IDCheckin.Request)
    ))
  ,

  Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), dict(
    DESCRIPTOR = _IDCHECKIN_OPERATION,
    __module__ = 'checkin.v1beta1.CheckinService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.checkin.v1beta1.IDCheckin.Operation)
    ))
  ,
  DESCRIPTOR = _IDCHECKIN,
  __module__ = 'checkin.v1beta1.CheckinService_Beta1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.checkin.v1beta1.IDCheckin)
  ))
_sym_db.RegisterMessage(IDCheckin)
_sym_db.RegisterMessage(IDCheckin.Request)
_sym_db.RegisterMessage(IDCheckin.Operation)

CardCheckin = _reflection.GeneratedProtocolMessageType('CardCheckin', (_message.Message,), dict(

  Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
    DESCRIPTOR = _CARDCHECKIN_REQUEST,
    __module__ = 'checkin.v1beta1.CheckinService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.checkin.v1beta1.CardCheckin.Request)
    ))
  ,

  Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), dict(
    DESCRIPTOR = _CARDCHECKIN_OPERATION,
    __module__ = 'checkin.v1beta1.CheckinService_Beta1_pb2'
    # @@protoc_insertion_point(class_scope:bloombox.schema.services.checkin.v1beta1.CardCheckin.Operation)
    ))
  ,
  DESCRIPTOR = _CARDCHECKIN,
  __module__ = 'checkin.v1beta1.CheckinService_Beta1_pb2'
  # @@protoc_insertion_point(class_scope:bloombox.schema.services.checkin.v1beta1.CardCheckin)
  ))
_sym_db.RegisterMessage(CardCheckin)
_sym_db.RegisterMessage(CardCheckin.Request)
_sym_db.RegisterMessage(CardCheckin.Operation)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n+io.bloombox.schema.services.checkin.v1beta1H\001P\001\242\002\003BBS'))

_CHECKIN = _descriptor.ServiceDescriptor(
  name='Checkin',
  full_name='bloombox.schema.services.checkin.v1beta1.Checkin',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1818,
  serialized_end=2394,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='bloombox.schema.services.checkin.v1beta1.Checkin.Ping',
    index=0,
    containing_service=None,
    input_type=_PING_REQUEST,
    output_type=_PING_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\027\022\025/checkin/v1beta1/ping')),
  ),
  _descriptor.MethodDescriptor(
    name='Identification',
    full_name='bloombox.schema.services.checkin.v1beta1.Checkin.Identification',
    index=1,
    containing_service=None,
    input_type=_IDCHECKIN_REQUEST,
    output_type=_CHECKINRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002_\"9/checkin/v1beta1/{scope=partners/*/locations/*}/global:id:\001*Z\037\"\032/checkin/v1beta1/global:id:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='Card',
    full_name='bloombox.schema.services.checkin.v1beta1.Checkin.Card',
    index=2,
    containing_service=None,
    input_type=_CARDCHECKIN_REQUEST,
    output_type=_CHECKINRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002!\"\034/checkin/v1beta1/global:card:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_CHECKIN)

DESCRIPTOR.services_by_name['Checkin'] = _CHECKIN

# @@protoc_insertion_point(module_scope)
